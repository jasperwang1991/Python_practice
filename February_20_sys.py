# python的保準庫中的sys模塊
# 對於這個模塊只是初步的瞭解，期待後續

import sys

"""
# 疑問：此處并沒有成功的導入脚本，實現如下的功能，不明白問題也不明白怎麽處理
print(sys.argv)   # 文件絕對路徑列表

print("script", sys.argv[0])  # 文件路徑字符串

if len(sys.argv) > 0:   # 返回的列表長度就是1
    # print(len(sys.argv))
    print("傳入的參數:", sys.argv[1:])   # 截取列表的長度
"""


# print("Python版本:", sys.version)   # 獲取python解釋器的版本

# sys.exit()常用於異常處理
print("程序開始···")
sys.exit("提前退出程序")
print("這行不會執行")
