def qtd_divisores(x):
    i=1
    s=[]
    while i <x:
        x%i==0
        s.append(i)
    i+=1
    return len(s)