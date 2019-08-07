# coding: utf-8
import gensim
model = gensim.models.Word2Vec.load("wiki.zh.text.model")
model.init_sims(replace = True)

result = model.most_similar("足球")
for e in result:
    print(e[0], e[1])

result = model.most_similar("男人")
for e in result:
    print(e[0], e[1])

result = model.most_similar("女人")
for e in result:
    print(e[0], e[1])

result = model.most_similar("青蛙")
for e in result:
    print(e[0], e[1])

result = model.most_similar("姨夫")
for e in result:
    print(e[0], e[1])

result = model.most_similar("衣服")
for e in result:
    print(e[0], e[1])

result = model.most_similar("公安局")
for e in result:
    print(e[0], e[1])

result = model.most_similar("铁道部")
for e in result:
    print(e[0], e[1])
result = model.most_similar("清华大学")
for e in result:
    print(e[0], e[1])

result = model.most_similar("卫视")
for e in result:
    print(e[0], e[1])

result = model.most_similar("习近平")
for e in result:
    print(e[0], e[1])

result = model.most_similar("林丹")
for e in result:
    print(e[0], e[1])

result = model.most_similar("语言学")
for e in result:
    print(e[0], e[1])

result = model.most_similar("计算机")
for e in result:
    print(e[0], e[1])

model.similarity("计算机", "自动化")

model.similarity("女人", "男人")

model.doesnt_match("早餐 晚餐 午餐 中心".split())

print(model.doesnt_match("早餐 晚餐 午餐 中心".split()))
