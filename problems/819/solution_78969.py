def filtraMultiplos(lista:list,inteiro:int)->list:
    return filter(lambda x: x%inteiro == 0, lista)