def freq_palavras(frases):
    """funcao recebe uma string e retorna ao dicionario para cada palavra string seja uma chave""""
    lista = frases.split(' ')
    dic = dict()
    for palavra in lista:
        dic[palavra] = lista.count(palavra)
    return dic