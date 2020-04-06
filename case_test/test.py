import sys

import requests

url = "http://10.100.10.198:8556/ias/master-api/calc/addOrUpdateIndicator"
payload ="{\"targetCodeParam\":\"[{\\\"calculatorsName\\\":\\\"经济活动人口_俄罗斯\\\",\\\"frequencyName\\\":\\\"月\\\",\\\"unit\\\":\\\"人\\\",\\\"indicatorCode\\\":\\\"190901040\\\",\\\"code\\\":\\\"A\\\"}]\",\"unit\":\"人\",\"indicatorName\":\"经济活动人口_俄罗斯\",\"targetCalcType\":0,\"formulaType\":\"FORMULA\",\"decicmalPlace\":\"1\",\"saveToIndicBase\":false,\"calcModeJson\":\"{\\\"formula\\\":\\\"10A\\\"}\"}"
headers = {
  'Authentication': 'f0813db7b7f3d2216b377562d75d13e52fc6837d859229ecf2437d698600214e14471b83adc2d846397b7c3c7b5477acf6db72277f7d3ec5761f78c10fff078cdad53c55f44de7eb18ac357a66a7dffd73b9598e8722f290a1c22f651d65113a14cbbd39b3127dc309da8c697245e34bbd541a070feafc984758bfe5d859eff9979bd93e7710676ce4b49856b046aeb0',
  'Accept': 'application/json, text/plain, */*',
  'Content-Type': 'application/json'
}
r=requests.post(url=url,data=payload.encode("utf-8"),headers=headers)
print(r.elapsed.total_seconds())
