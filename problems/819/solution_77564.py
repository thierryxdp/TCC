def filtraMultiplos(list,numero):
    posicao=0
    list=[]
    while posicao<len(list):
        if list[posicao]%numero==0:
            list=list+list[posicao]
        posicao=posicao+1
    return list