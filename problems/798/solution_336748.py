def freq_palavras(frases):
    '''
    	Função que recebe uma frase e retorna um dicionário, sendo a chave cada palavra dessa frase e o valor a quantidade que essa palavra se repete
        str -> dict
    '''
    lista = str.split(frases)
    dicionario = {}
    for i in range(len(lista)):
        dicionario[lista[i]] = list.count(lista,lista[i])
    return(dicionario)