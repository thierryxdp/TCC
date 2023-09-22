def intercala(lista1, lista2):
    """Função que dadas duas listas de tamanho 3, retorna uma lista nova intercalando os itens das lista1 e lista2"""
    return [*sum(zip(lista1,lista2),())]