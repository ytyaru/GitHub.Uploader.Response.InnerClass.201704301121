class Response(object):
    class __Headers(object):
        class __ContentType(object):
            class __MimeType(object):
                class __SubType(object):
                    pass


if __name__ == '__main__':
    r = Response()
    h = r._Response__Headers()
    c = h._Headers__ContentType()
    m = c._ContentType__MimeType()
    s = m._MimeType__SubType()

