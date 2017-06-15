class Response(object):
    def __init__(self):
        self.__headers = self._Response__Headers()
    @property
    def Headers(self):
        return self.__headers
    class __Headers(object):
        def __init__(self):
            self.__content_type = self._Headers__ContentType()
        @property
        def ContentType(self):
            return self.__content_type
        class __ContentType(object):
            def __init__(self):
                self.__mime_type = self._ContentType__MimeType()
            @property
            def MimeType(self):
                return self.__mime_type
            class __MimeType(object):
                def __init__(self):
                    self.__sub_type = self._MimeType__SubType()
                @property
                def SubType(self):
                    return self.__sub_type
                class __SubType(object):
                    pass


if __name__ == '__main__':
    r = Response()
    h = r._Response__Headers()
    c = h._Headers__ContentType()
    m = c._ContentType__MimeType()
    s = m._MimeType__SubType()

    print(r)
    print(r.Headers)
    print(h.ContentType)
    print(c.MimeType)
    print(m.SubType)

    #<__main__.Response.__Headers object at 0x00000001>
    #<__main__.Response.__Headers.__ContentType object at 0x00000002>
    #<__main__.Response.__Headers.__ContentType.__MimeType object at 0x00000003>
    #<__main__.Response.__Headers.__ContentType.__MimeType.__SubType object at 0x00000004>


