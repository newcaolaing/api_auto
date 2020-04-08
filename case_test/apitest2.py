import re
import sys
import unittest



from base.api_method import RunMethod
from config.setting import api_excel_path, logging, qjbl, headers
from util import paramunittest
from util.Variate import Variate
from util.exl import Excel_Opertion
api_excel= Excel_Opertion(api_excel_path)
test_case= api_excel.get_data()



# url
base_url='http://'+sys.argv[1]



@paramunittest.parametrized(*test_case)
class TestDemo(RunMethod):
    def setParameters(self,TEST_ID,TEST_NAME,MODULE,method,headers,url,data,eq,variate,isshow):
        '''这里注意了，user, psw, result三个参数和前面定义的字典一一对应'''
        self.test_name = TEST_NAME
        self.TEST_ID = TEST_ID
        self.module = MODULE
        self.method = method
        self.headers = headers
        self.variate = variate
        self.isshow = isshow
        self.data = data
        self.url = url
        self.eq = eq


    def testcase(self):

        self.__class__.__qualname__=self.module+"_"+self.TEST_ID
        self._testname = self.test_name
        self._testid= self.TEST_ID

        # 头部信息获取
        if "json" in self.headers and "json" not in str(headers) :
            headers["Content-Type"] = "application/json"
        if "json" not in self.headers and "json"  in str(headers):
            headers.pop("Content-Type")


        logging.info("开始执行用例：----"+self.test_name)
        # 头部变量信息获取
        Variate().variate(self.variate)
        # 判断data中是否需要将变量替换
        self.data = Variate().judge(self.data)
        logging.info("当前请求数据为 ： " + str(self.data))

        print("请求url为："+base_url + self.url )
        print("请求内容为："+str(self.data) )
        r = self.run_request(self.method, base_url + self.url, data=self.data,
                             header=headers)

        print("请求的完整url："+ r.url)
        print("当前返回数据："+r.text)
        logging.info("当前返回数据为 ：" + str(r.json()))

        # 采集变量信息
        Variate().variate(self.variate, r)

        results = self.api_assert(r, self.eq)
        logging.info(results)
        for result in results:
            self.assertTrue(result)



    # 断言判断
    def api_assert(self,r, eqs):
        RESULT = []
        eqs=Variate().judge(eqs)
        eqs=int(eqs) if  type(eqs) is float  else eqs
        eq = str(eqs).split("||")
        for e in eq:

            print("当前正则匹配规则：" + e)
            # 判断response返回码
            if  type(eqs) is float or  (e.isdigit() and len(e) == 3) :
                print("接口状态码：" +str(r.status_code)+ ",预期结果" + e)
                if r.status_code  == int(e):
                    RESULT.append(True)
                else:
                    RESULT.append(False)
                    raise Exception("状态码验证不成功")
            # 完全等于
            elif ":=" in e:
                e=e.strip(":=")
                print("接口返回：" + str(r.text) + ",预期结果" + e)
                if r.text == e:
                    RESULT.append(True)
                else:
                    RESULT.append(False)
                    raise Exception("response返回数据不相等 ："+e)

            # 正则匹配内容规则
            elif "pattern" in e:

                if re.findall("pattern\d", e):
                    nums = re.findall("pattern(\d*?)\s", e)[0]
                    p = e.strip("pattern" + nums + " ")
                    print("response正则匹配文本期望次数需要大于等于" + nums + ",当前匹配次数为：" + str(len(re.findall(p, r.text))))
                    if len(re.findall(p, r.text)) >= int(nums):
                        RESULT.append(True)
                        logging.info("response正则匹配文本期望次数需要大于等于" + nums + ",当前匹配次数为：" + str(len(re.findall(p, r.text))))
                    else:
                        RESULT.append(False)
                        raise Exception("response正则匹配文本期望次数需要大于等于" + nums + ",当前匹配次数为：" + str(len(re.findall(p, r.text))))
                else:
                    e = e.strip("pattern ")
                    print("当前匹配规则：" + e )
                    if re.findall(e,r.text):
                        RESULT.append(True)
                    else:
                        RESULT.append(False)
                        raise Exception("respons返回数据格式与正则不匹配 ：" + e[:20]+"...")

            # 内容长度大于
            elif "len" in e:
                e=e.strip("len ")
                print("内容长度" + str(len(r.text)) + ",预期长度需大于" + e)
                if len(r.text) >= int(e):
                    RESULT.append(True)
                else:
                    RESULT.append(False)
                    raise Exception("respons返回数据长度小于" + e)

            # 不包含关键字
            elif "not" in e:
                e=e.strip("not ")
                print("判断当返回不包含："+ e )
                if e not in r.text:
                    RESULT.append(True)
                else:
                    RESULT.append(False)
                    raise Exception("respons返回数据包含:" + e)


            # 包含
            else:
                print("判断返回内容是否包含:" + e)
                if e in r.text:
                    RESULT.append(True)
                else:
                    RESULT.append(False)
                    raise Exception("respons返回数据没有包含:" + e)

        return RESULT


if __name__ == '__main__':
    unittest.main()