def faltante(lista):
    soma=sum(lista)
    maior=max(lista)
    item=0
    completa=[]
    while item<=maior:
        completa.append(item)
        item+=1
    soma2=sum(completa)
    if soma2-soma>0:
        return (soma2-soma)
    if soma2-soma==0:
        return maior+1