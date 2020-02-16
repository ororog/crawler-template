# urllib の使い方 https://qiita.com/hoto17296/items/8fcf55cc6cd823a18217
import urllib.request
# 正規表現 の使い方 https://note.nkmk.me/python-re-match-search-findall-etc/
import re
import json

URL = 'https://t.pia.jp/pia/event/event.do?eventCd=1954319&afid=L28'


def crawl_handler(event, context):
    req = urllib.request.Request(URL)
    with urllib.request.urlopen(req) as res:
        body = res.read()
        if re.search(r'受付', body.decode('utf-8')):
            print('受付中')
            # 条件にマッチしたときの処理
            # slack に通知がおすすめ
            # https://qiita.com/sudo5in5k/items/947f0bf6450ac7435a9c
            SLACK_WEBHOOK = ''
            data = {
                'text': 'found'
            }

            headers = {
                'Content-Type': 'application/json',
            }

            req = urllib.request.Request(
                SLACK_WEBHOOK, json.dumps(data).encode(), headers)
            with urllib.request.urlopen(req) as res:
                body = res.read()


if __name__ == '__main__':
    crawl_handler(None, None)
