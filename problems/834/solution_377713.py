def media_matriz(lista):
    x=0
    soma=0
    y = len(lista)
    while x < y:
               soma = (soma + sum(lista[x]))
               x=x+1
               
                   
    dividir=len(lista[0]) * y 
    resultado =soma/dividir
    return round(resultado,2)
"""retorna a media de todos os numeros de uma matriz com duas casas de precisão, list->float"""