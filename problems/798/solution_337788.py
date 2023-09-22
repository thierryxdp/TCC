def freq_palavras(frases):
    """ função que retorna a quantidade de vezes que uma palavra
    foi repetida numa frase
    :frases ---> str:
    :return ---> dict: 
    """
    lista = str.split(frases)
    i = 0
    dicio = {}
    while i < len(lista):
        chave = lista[i]
        valor = list.count(lista, lista[i])
        dicio[chave] = valor
        i += 1
    return dicio