def intercala(lista1, lista2):
    """Retorna a intercalação das listas 1 e 2"""
    
    intercalacao = [lista1 + lista2] 
    lista3 = list.sort(intercalacao)
    return lista3