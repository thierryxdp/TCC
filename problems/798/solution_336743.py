def freq_palavras(frases):
    '''
    	Função que recebe uma frase e retorna um dicionário, sendo a chave cada palavra dessa frase e o valor a quantidade que essa palavra se repete
        str -> dict
    '''
    lista = str.split(frases)
    lista_key = []
    for i in lista:
        lista_key = list.append(list.count(lista,lista[i]))
    return (lista_key)