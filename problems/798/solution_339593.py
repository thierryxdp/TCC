# Coloque def freq_palavras(frases):
    lista = frases.split(' ')
    dic = dict()
    
    contador = 0
    while contador < len(lista):
        x = lista[contador]
        dic[x] = lista.count(x)
        contador = contador + 1
    
    #for x in lista:
    #    dic[x] = lista.count(x)
    
    
    return dicum comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis