def repetidos (lista_num):
    """função que recebe uma lista numérica (lista_num) e que deve
    analisar a lista e retornar o número de vezes que um elemento da
    da lista é repetido: len<qtd_num>;
    lista->int"""
    i = 0
    qtd_num = []
    while i<len(lista_num[:-1]):
        if lista_num[i]==lista_num[i+1]:
            qtd_num = qtd_num + [lista_num[i]]
        i = i + 1
    return len(qtd_num)