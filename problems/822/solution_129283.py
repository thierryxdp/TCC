def repetidos(lista):
    """Função que dada uma lista de números, verifica quantas repetições há de números consecutivos que se repetem. list ->int"""
    numero = 0
    for r in range(len(lista)-1):
        if lista[r] == lista[r+1]:
            numero += 1
    return numero