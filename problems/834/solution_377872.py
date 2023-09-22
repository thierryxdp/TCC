def media_matriz (lista):
    soma = 0
    naonula = 0
    tamanho = len(lista)
    for x in lista:
        if (x < tamanho):
            soma += sum(lista[x])
        
    
    return soma