#coding:utf-8
import requests
import json

from base.myunit import StartEnd
from config.setting import logging


class RunMethod(StartEnd):

	def post_main(self,url,data,header=None):
		res = None
		print(type(data))
		print(json.loads(data.encode()))
		if header !=None:
			res = requests.post(url=url,data=data.encode("utf-8"),headers=header)
		else:
			res = requests.post(url=url,data=json.loads(data))
		# return res.json()
		return res

	def get_main(self,url,data=None,header=None):
		res = None
		if header !=None:
			res = requests.get(url=url,data=data,headers=header,verify=False)
		else:
			res = requests.get(url=url,data=data,verify=False)
		return res


	def postp_main(self,url,data,header=None):
		res = None
		if header !=None:
			if data:
				res = requests.post(url=url,params=json.loads(data),headers=header)
			else:
				res = requests.post(url=url, headers=header)
		else:
			res = requests.post(url=url,params=json.loads(data))
		# return res.json()
		return res

	def getp_main(self,url,data=None,header=None):
		res = None
		if header !=None:
			if data:
				res = requests.get(url=url,params=json.loads(data),headers=header,verify=False)
			else:
				res = requests.get(url=url,headers=header, verify=False)
			print(res.url)
		else:
			res = requests.get(url=url,params=data,verify=False)
		return res


	def run_request(self,method,url,data=None,header=None):
		logging.info("当前正在请求的url:" + url)
		if "json" in str(header):
			res = None
			if method == 'Post':
				res = self.post_main(url,data,header)
			else:
				res = self.get_main(url,data,header)
			# return json.dumps(res,ensure_ascii=False)
			return res
		else:
			res = None
			if method == 'Post':
				res = self.postp_main(url,data,header)
			else:
				res = self.getp_main(url,data,header)
			# return json.dumps(res,ensure_ascii=False)
			return res



