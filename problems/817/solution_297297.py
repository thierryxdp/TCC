def notas(notas):
    soma=sum(notas)
    divisor=len(notas)
    k=soma/divisor
    notas.sort()
    indice=list.index(notas,k)
    return lista[indice+1:]