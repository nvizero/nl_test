import jieba

sentence = "我爱自然语言处理"
words = jieba.cut(sentence, cut_all=False) # 精确模式分词，适合文本分析

for word in words:
    print(word)

