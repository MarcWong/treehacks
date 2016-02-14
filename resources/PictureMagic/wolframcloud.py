from urllib import urlencode
from urllib2 import urlopen

class WolframCloud:
    def wolfram_cloud_call(self, **args):
        arguments = dict([(key, arg) for key, arg in args.iteritems()])
        result = urlopen("http://www.wolframcloud.com/objects/39a0a27c-b5a3-4560-bc6d-9c2359af0dfa", urlencode(arguments))
        return result.read()

    def call(self, x):
        textresult = self.wolfram_cloud_call(x=x)
        return textresult

'''
a = WolframCloud()
b = a.call("https://encrypted-tbn3.gstatic.com/images?q=tbn:ANd9GcTrr-mRP7ilbFgeuP4Q_gJb5HOeE_tdRxj29y5Gy8du6WKtzxMCOuDOykdy")
print type(b)
print repr(b)
print str(b)
'''
