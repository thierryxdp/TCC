def eh_quadrada(lista):
    '''Função que recebe uma matriz e retorna uma expressão booleana
    Entrada(lista)
    Saída(bool)'''
    if len(lista)==0:
        return True
    elif len(lista)==len(lista[0]):
        return True
    else:
        return False