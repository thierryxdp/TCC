def busca(Procurar, Matriz):
    '''Função que dada uma matriz e uma palavra,
    procura as pessoas que cumprem o requisito escolhido; str, list -> list'''
    lista = []
    for linha in Matriz:
        if Procurar in linha:
            linha.remove(Procurar)
            lista += [linha]
    return lista