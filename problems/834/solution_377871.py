def media_matriz (lista):
    soma = 0
    naonula = 0
    for x in lista:
        if (x < len(lista)):
            soma += sum(lista[x])
        
    
    return soma