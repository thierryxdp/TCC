def media_matriz(lista):
    x=0
    soma=0
    y = len(lista)
    while x < y:
               soma = (soma + sum(lista[x]))/ len(lista[x])
               x=x+1
               
                   
    return soma