def freq_palavras(frase):
    ''' a seguinte função irá receber a frase e retornar um dicionário 
    com a quantidade de cada palavra da string. str--> dict'''

    lista_palavras = frase.split() 
    dict1 = {}  
    contador = 0  

    for palavra in lista_palavras:
        dict1[lista_palavras[contador]] = lista_palavras.count(lista_palavras[contador]) #insere elemento no dicionário
        contador += 1

    return dict1