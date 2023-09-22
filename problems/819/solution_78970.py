def filtraMultiplos(lista:list,inteiro:int)->list:
    return list(filter(lambda x: x%inteiro == 0, lista))