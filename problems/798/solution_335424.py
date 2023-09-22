def freq_palavras(string):
    x = str.split(string," ")
    k = 0
    z = {}
    while k < len(x):
       f = list.count(x,x[k])
       z[x[k]] = f
       k = k + 1
    return z