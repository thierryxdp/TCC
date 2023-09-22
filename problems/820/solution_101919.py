def posLetra(st,lt,num):
    'retorna a posicao e uma letra dado o numero pedido; str,str,int->int'
    lista=[st]
    a=0
    lista1=[]
    while a<len(st):
        if st[a]==lt:
            lista1=lista1+[a]
        a=a+1
    if len(lista1)<num:
        return 1
    return lista1[num-1]