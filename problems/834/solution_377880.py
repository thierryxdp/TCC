def media_matriz (lista):
    soma = 0
    naonulo = 0
    tamanho = len(lista)
    while naonulo < tamanho:
        soma += sum(lista[naonulo])
    	naonulo += 1
    
    divisao = y * len(lista[0])
    return round((soma/divisao), 2)