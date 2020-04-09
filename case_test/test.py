import json
import re

a = """
{
"name":"test",
"dict": {"list":[{"c":"a"},{"c":"a"},{"c":"a"}},
"list": [{"name":"dict1"},{"name":"dict2"}],
"list2":[,2,3,"1111"]
}
"""


b  =re.sub("[^{}[\]]","",a)
print("只获取结构："+ b)

c= re.sub("(\[)([^{}\[\]]*?)(\])",r"\1\3",re.sub("(:\".*?\")|\s","",a))
print("获取key和结构："+c)

