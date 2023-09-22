def faltante(L):
    contador=0
    variavel=list(range(1,Len(L)+2))
    list.sort(L)
    while contador<len(L):
        if variavel[-1]==L[-1]+1:
            return variavel[-1]
        if L[contador]==variavel[contador]:
            contador+=1
        else:
            return variavel[contador]