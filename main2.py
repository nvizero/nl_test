from ckiptagger import data_utils, construct_dictionary, WS
# 加载模型

#data_utils.download_data_gdown("./ckiptagger/")  # 將資料檔案下載到當前目錄

ws = WS("./ckiptagger/data")

sentence_list = ["我爱自然语言处理"]

word_sentence_list = ws(sentence_list)

for word in word_sentence_list[0]:
    print(word)
