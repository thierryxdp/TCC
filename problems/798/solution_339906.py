def freq_palavras(string):
    var1=string.split()
    var={}
    for e in var1:
        if e in var:
            var[e]+=1
        else:
            var[e]=1
    return var