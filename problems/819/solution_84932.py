def filtraMultiplos(lista_num, num):
    """Retorna uma nova lista com todos elementos da lista de entrada, exceto pelos multiplos do numero da entrada
    list, float -> list"""
    cont = 0
    lista_retorno = []
    while cont < len(lista_num):
        if lista_num[cont] % num == 0:
        	lista_retorno += [lista_num[cont],]  
        cont++
    return lista_retorno