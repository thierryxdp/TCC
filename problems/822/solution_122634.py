def repetidos(x):
    i=0
    vogais=[]
    while len(x) > i:    
        if x[-1]==x[i] or x[i]==x[i+1]:
            vogais= vogais + [1]
            i=i+1
        elif x[i] != x[i+1] or i != x.index(x[i]):
            i=i+1
    return len(vogais)/2