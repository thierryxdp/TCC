def total(lista,dicionario):
    """FUNÇÃO QUE RETORNA O VALOR TOTAL
    DOS ITENS DA LISTA QUE ESTEJAM DISPONÍVEIS
    LIST,DICT=>FLOAT"""
    soma=0
    for i in lista:
        if i in dicionario:
            soma= soma + dicionario[i]
    return round(soma,2)