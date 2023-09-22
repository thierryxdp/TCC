def faltante (lista):
    '''funcao que diz quantas pecas falta int -> int '''
    l= lista[:]
    l.sort()
    contador=0
    peca=-1
    while contador<len(l):
        if l[contador]==contador+1:
            contador+=1
        else:
            pecas = contador+1
            contador = len(l)
    if peca==-1:
        peca=len(l)+1
   
    return peca