import copy

class Url:
    def __init__(self, scheme=None, authority=None, path=None, query=None, fragment=None):
        self.scheme = scheme
        self.authority = authority
        self.path = path
        self.query = query
        self.fragment = fragment

    def __str__(self):
        res = str(self.scheme) + '://' + str(self.authority)
        if self.path:
            for i in self.path:
                res += '/' + str(i)
        if self.query:
            res += '?'
            q = 0
            for i,j in self.query.items():
                if q == 0:
                    res += str(i) + '=' + str(j)
                else:
                    res += '&' + str(i) + '=' + str(j)
                q+=1
        if self.fragment:
            res += str(self.fragment)
        return res

    def __eq__(self, other):
        return str(self) == other


class HttpsUrl(Url):
    def __init__(self, *args, **kwargs):
        super().__init__(self, *args, **kwargs)
        self.scheme = 'https'


class HttpUrl(Url):
    def __init__(self, *args, **kwargs):
        super().__init__(self, *args, **kwargs)
        self.scheme = 'http'


class GoogleUrl(HttpsUrl):
    def __init__(self, *args, **kwargs):
        super().__init__(self, *args, **kwargs)
        self.authority = 'google.com'


class WikiUrl(HttpsUrl):
    def __init__(self, *args, **kwargs):
        super().__init__(self, *args, **kwargs)
        self.authority = 'wikipedia.org'


class UrlCreator(Url):
    def _create(self):
        return self

    def __getattr__(self, item):
        if self.path:
            new_path = self.path
            new_path.append(str(item))
        else:
            new_path = []
            new_path.append(str(item))
        return UrlCreator(scheme=self.scheme, authority=self.authority, path=new_path, query=self.query, fragment=self.fragment)

    def __call__(self, *args, **kwargs):
        if args:
            self.path = list(args)
        if kwargs:
            self.query = kwargs
        return self


assert GoogleUrl() == HttpsUrl(authority='google.com')
assert GoogleUrl() == Url(scheme='https', authority='google.com')
assert GoogleUrl() == 'https://google.com'
assert WikiUrl() == str(Url(scheme='https', authority='wikipedia.org'))
assert WikiUrl(path=['wiki', 'python']) == 'https://wikipedia.org/wiki/python'
assert GoogleUrl(query={'q': 'python', 'result': 'json'}) == 'https://google.com?q=python&result=json'


url_creator = UrlCreator(scheme='https', authority='docs.python.org')
assert url_creator.docs.v1.api.list == 'https://docs.python.org/docs/v1/api/list'
assert url_creator('api','v1','list') == 'https://docs.python.org/api/v1/list'
assert url_creator('api','v1','list', q='my_list') == 'https://docs.python.org/api/v1/list?q=my_list'
assert url_creator('3').search(q='getattr', check_keywords='yes', area='default')._create()  == 'https://docs.python.org/3/search?q=getattr&check_keywords=yes&area=default'