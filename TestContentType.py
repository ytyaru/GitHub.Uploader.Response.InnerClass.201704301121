import unittest
from Response import Response
import requests
class TestResponse(unittest.TestCase):
    def test_GitHubApiDefault(self):
        top_level_type = 'application'
        sub_type = 'json'
        mime_type = '{top_level_type}/{sub_type}'.format(top_level_type=top_level_type, sub_type=sub_type)
        char_set = 'utf-8'
        content_type = '{mime_type}; charset={char_set}'.format(mime_type=mime_type, char_set=char_set)
        response = Response()
#        c = Response.__Headers.__ContentType(content_type)

        res = requests.Response()
        res.headers = {}
        res.headers['Content-Type'] = '{mime_type}; charset={char_set};'.format(mime_type=mime_type, char_set=char_set)
        h = response._Response__Headers(res)
        c = h._Headers__ContentType(content_type)
        self.assertEqual(content_type, c.String)
        print(c.String)
        print(c.MimeType.TopLevelType)
        print(c.MimeType.String)
        self.assertEqual(mime_type, c.MimeType.String)
        self.assertTrue('charset' in c.Parameters.keys())
        self.assertEqual(char_set, c.Parameters['charset'])
        self.assertEqual(top_level_type, c.MimeType.TopLevelType)
        self.assertEqual(sub_type, c.MimeType.SubType.String)
        self.assertEqual(None, c.MimeType.SubType.Facet)
        self.assertEqual(None, c.MimeType.SubType.Suffix)
        self.assertEqual(sub_type, c.MimeType.SubType.MediaType)
"""        
    def test_MultiParameter(self):
        # https://ja.wikipedia.org/wiki/%E3%83%A1%E3%83%87%E3%82%A3%E3%82%A2%E3%82%BF%E3%82%A4%E3%83%97#.E5.91.BD.E5.90.8D.E8.A6.8F.E5.89.87
        top_level_type = 'text'
        sub_type = 'plain'
        mime_type = '{top_level_type}/{sub_type}'.format(top_level_type=top_level_type, sub_type=sub_type)
        char_set = 'iso-2022-jp'
        res = requests.Response()
        res.headers = {}
        res.headers['Content-Type'] = '{mime_type}; charset={char_set}; format=flowed; delsp=yes'.format(mime_type=mime_type, char_set=char_set)
        c = Response.Headers.ContentType()
        c.Split(res)
        self.assertEqual(mime_type, c.mime_type)
        self.assertEqual(top_level_type, c.top_level_type)
        self.assertEqual(sub_type, c.sub_type)
        self.assertEqual(char_set, c.char_set)
        self.assertTrue('charset' in c.parameters.keys())
        self.assertEqual(char_set, c.parameters['charset'])
        self.assertTrue('format' in c.parameters.keys())
        self.assertEqual('flowed', c.parameters['format'])
        self.assertTrue('delsp' in c.parameters.keys())
        self.assertEqual('yes', c.parameters['delsp'])
        self.assertEqual(None, c.suffix)

    # バグ発見。suffixが取得できていなかった。
    def test_Suffix(self):
        # https://developer.github.com/v3/media/
        top_level_type = 'application'
        suffix = 'json'
        # サブタイプ名はツリー、サブタイプ名、サフィックスに分けられるらしい。が、細かすぎるのでまとめてサブタイプ名とした。
        # https://ja.wikipedia.org/wiki/%E3%83%A1%E3%83%87%E3%82%A3%E3%82%A2%E3%82%BF%E3%82%A4%E3%83%97#.E5.91.BD.E5.90.8D.E8.A6.8F.E5.89.87
        sub_type = 'vnd.github.v3+{suffix}'.format(suffix=suffix)
        mime_type = '{top_level_type}/{sub_type}'.format(top_level_type=top_level_type, sub_type=sub_type)
        char_set = 'utf-8'
        res = requests.Response()
        res.headers = {}
        res.headers['Content-Type'] = '{mime_type}; charset={char_set}'.format(mime_type=mime_type, char_set=char_set)
        c = Response.Headers.ContentType()
        c.Split(res)
        self.assertEqual(mime_type, c.mime_type)
        self.assertEqual(top_level_type, c.top_level_type)
        self.assertEqual(sub_type, c.sub_type)
        self.assertEqual(char_set, c.char_set)
        self.assertTrue('charset' in c.parameters.keys())
        self.assertEqual(char_set, c.parameters['charset'])
        self.assertEqual(suffix, c.suffix)
"""
