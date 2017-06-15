class ContentType(object):
    def __init__(self):
#        self.__mime_type = ContentType.MimeType()
        self.__mime_type = ContentType.__MimeType()
    @property
    def MimeType(self):
        return self.__mime_type
#    class MimeType(object):
    class __MimeType(object):
        @property
        def String(self):
            return 'MimeType String Property.'


if __name__ == '__main__':
    c = ContentType()
    print(c.MimeType.String) # class名とproperty名が重複しているせいでclass名のほうを参照してしまう
    # 期待値: 'MimeType String Property.'
    # 実際値: <property object at 0xb70e8c0c>    プロパティ定義のポインタ

    # プライベートなクラスでも以下のように書けばアクセスできてしまう。
    m = c._ContentType__MimeType()
    print(m.String)
