def primo (n) :
    """Funcao que retorna um dado booleano de um numero inteiro indicando se ele e um numero primo ou não"""
    lista = []
    for i in range(2, n+1) :
        if n%i == 0 :
            list.append(lista, i)
    if len(lista)==1:
        return True
    else :
        return False