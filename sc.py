from bs4 import BeautifulSoup
import requests
from linebot import LineBotApi
from linebot.models import TextSendMessage

def check():
    url = "https://takaken.tokyo"
    res = requests.get(url)
    soup = BeautifulSoup(res.text, "html.parser")
    old_file = "old_elem.txt"

    # 今回取り込んだ情報を取り出す
    new_elem = str(soup.select(".articles")
                   [0].select(".mrow")[0].select(".mcol")[0].select(".title")[0].get_text())
    # new_elem = str(soup.select(".theme-doc-markdown")[0].select("a")[1].get_text())

    # 前回のデータを取り込む
    try:
        with open(old_file) as f:
            old_elem = f.read()
    except:
        old_elem = ""

    if new_elem == old_elem:
        return False
    else:
        with open(old_file, "w") as f:
            f.write(new_elem)
        return f"新しい記事が投稿されました！\n【{new_elem}】\n{url}"


# メッセージを送る
def send_line(access_token, talk):
    # メッセージ送信用に変換
    message = TextSendMessage(text=talk)

    # secretsに登録した環境変数の呼び出し
    # LINEbotにトークンを入力
    line_bot_api = LineBotApi(access_token)
    # LINEbotでメッセージを送る
    # line_bot_api.push_message(user_id, messages=message)
    # bot友達の全員に送信
    line_bot_api.broadcast(messages=message)
