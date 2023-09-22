def faltante(lista):
    soma=sum(lista)
    maior=max(lista)
    item=0
    completa=[]
    while item<=maior:
        completa.append(item)
        item+=1
    soma2=sum(completa)
    return (soma2-soma)