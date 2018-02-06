from yandex import Translater
tr = Translater()
'https://translate.yandex.net/api/v1.5/tr.json/translate ?'
tr.set_key('trnsl.1.1.20171122T165405Z.fa5d2c5f493284e0.0ff459ef353ee4d31bcd4bddbca34327e88e7678') # Api key found on https://translate.yandex.com/developers/keys
tr.set_text('hello world')
tr.set_from_lang('en')
tr.set_to_lang('ko')
print(tr.translate())
