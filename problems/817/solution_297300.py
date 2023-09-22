def acima_da_media(notas):
    soma=sum(notas)
    divisor=len(notas)
    k=soma/divisor
    k in notas
    notas.sort()
    indice=list.index(notas,k)
    return lista[indice+1:]