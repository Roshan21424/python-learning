'''enumerate(iterable) takes any list (or string, or anything iterable) and returns pairs of:(index,value)'''
vocab="hello,nice to meet you"
for i,ch in enumerate(vocab):
    print(i,ch)