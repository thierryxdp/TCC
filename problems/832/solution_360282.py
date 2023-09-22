def eh_quadrada(lista):
    if lista == []:
        return True
    linhas = len(lista)
    colunas = len(lista[0])
    if linhas == colunas:
        return True
    if lista[0] == []:
        return True
    else:
        return False