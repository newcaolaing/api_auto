# 定义变量获取
import json
import re

from config.setting import logging, headers, qjbl


class Variate():

    # 变量替换
    def judge(self,name):

        pattern =   re.findall("{{(.*?)}}",name)
        if pattern:
            for s in pattern:
                # 判断变量名称是否存在
                if qjbl.get(s):
                    name=re.sub(r"{{"+s+"}}",qjbl[s],name)
                    logging.info(s+" 变量替换为"+qjbl[s])
                else:
                    logging.error(s+" 在变量池中未找到")
            return name
        else:
            logging.info("暂无变量替换")
            return name

    # 变量添加
    def variate(self, name, response=None):
        logging.info("正在添加变量"+name)
        if name:
            try:
                site, key, value = re.split(r"[:：]=", name)
                # 请求头部添加变量信息
                if site == "header":
                    headers[key] = value

                # 提取response中的变量
                if site == "response-data" and response:
                    logging.info(json.dumps(response.json()))
                    logging.info(response.text)
                    pattern = re.findall(value, json.dumps(response.json(), ensure_ascii=False))
                    if not pattern:
                        pattern=re.findall(value, response.text)

                    logging.info(pattern)
                    if pattern:
                        qjbl[key] = pattern[0]
                        # 头部信息添加token
                        if key == "Authentication":
                            headers[key] = pattern[0]
                        logging.info("添加变量成功：" + str(qjbl))

                #用户自定义变量
                elif site == "user-data":
                        qjbl[key] = value



            except:
                logging.error(name + " 变量定义失败 ")