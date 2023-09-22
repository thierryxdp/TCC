def acima_da_media(lista):
    #retorna os valores que estão acima da média (que é a a metade da quantidade de numeros na lista)
    import math
    lista.sort()
    media= math.ceil(len(lista)/2 )
    resultado = lista[media:]
    return (resultado)