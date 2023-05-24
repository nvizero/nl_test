import jieba
from ckiptagger import WS

# Jieba 分词
sentence = "我爱自然语言处理"
jieba_words = jieba.cut(sentence, cut_all=False)
print(f"Jieba 分词结果: {list(jieba_words)}")

# CKIPtagger 分词
ws = WS("./ckiptagger/data")
sentence_list = [sentence]
ckip_words = ws(sentence_list)
print(f"CKIPtagger 分词结果: {ckip_words}")

