from sc import *
import os

if __name__ == "__main__":

    # 環境変数の取り込み
    access_token = os.environ['ACCESS_TOKEN']

    data = check()
    if data != False:
        send_line(access_token, data)
    else:
        pass
