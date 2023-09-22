def concatenacao(a,b):
    funcao=(a,b)
    return funcao[0]+ funcao[-1]+ funcao[-1] + funcao[0]
def substitui(s,x,i):
    s = s[0:i] + x + s[i+1:]
    return s
def recursiva(s):
    contador=((len(s))//2)
    return s[0:contador] + s + s[contador:]
def hashtag(s):
    contador = len(s)//2
    tag='#'
    return tag + s[0:contador] + tag + s[contador:] + tag
def filtra_pares(a,b,c,d):
    pares =()
    if a%2==0:
        pares += (a,)        
    if b%2==0:
        pares += (b,)
    if c%2==0:
        pares += (c,)
    if d%2==0:
        pares += (d,)
    return pares
Start your python function here