from sc import *
import os

if __name__ == "__main__":

    # 環境変数の取り込み
    access_token = os.environ['ACCESS_TOKEN']
    # access_token = "test"
    data = check()
    if data != False:
        send_line(access_token, data)
        print("更新されていました")
    else:
        print("更新されていませんでした。")
