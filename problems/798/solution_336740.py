def freq_palavras(frases):
    '''
    	Função que recebe uma frase e retorna um dicionário, sendo a chave cada palavra dessa frase e o valor a quantidade que essa palavra se repete
        str -> dict
    '''
    lista = str.split(frase)
    lista_key = []
    for i in lista:
        lista_key = list.count(lista,lista[i])
    return dict(lista,lista_key)