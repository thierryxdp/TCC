def eh_quadrada(lista:list)->bool:
    """Função que verifica se uma matriz é quadrada,
    ou seja, se possui o mesmo número de linhas e colunas ou se é vazia"""
    
    if lista==[]:
        return True
    if len(lista[0])==len(lista):
        return True
    else:
        return False