def substitui(s,x,i):
    palavra = s
    a = (len(s)-i)
    return palavra [0: i] + str (x) + palavra [-a: -1]