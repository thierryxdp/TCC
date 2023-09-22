def filtraMultiplos(lista:list,inteiro:int)->list:
    """Filtra da lista os números divisíveis por um inteiro dado"""
    return list(filter(lambda x: x%inteiro == 0, lista))