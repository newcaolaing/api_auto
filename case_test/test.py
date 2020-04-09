import json
import re

a = """
{
"name":"test",
"dict": {"list":[{"c":"a"},{"c":"a"},{"c":"a"}},
"list": [{"name":"dict1"},{"name":"dict2"}],
"list2":[1,2,3,"1111"]
}
"""


b  =re.sub("[^{}[\]]","",a)
print(b)


c= re.sub("(:\".*?\")","",a)
c= re.sub("(\[)([^{}\[\]]*?)(\])","\1\3",c)
print(c)

