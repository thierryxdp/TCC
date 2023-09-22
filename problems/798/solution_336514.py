def freq_palavras(frase):
    '''função recebe frase e retorna dicionário com
    quantidade de cada palavra da string.
    str--> dict'''

    lista_palavras = frase.split()  #cria lista com palavras da frase
    dict1 = {}  #cria dicionário vazio
    contador = 0  #inicia contador em zero

    for palavra in lista_palavras:  #para cada palavra na lista de palavras:
        dict1[lista_palavras[contador]] = lista_palavras.count(lista_palavras[contador]) #insere elemento no dicionário
        contador += 1  #incrementa contador

    return dict1  #retorna dicionário