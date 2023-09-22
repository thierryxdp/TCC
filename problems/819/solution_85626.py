def filtraMultiplos(lista,numero):
    '''list,int -> list'''
    '''retorna uma lista apenas com os numeros que são divisiveis por numero'''
    
    multiplos = []
    i = 0
    
    while i < len(lista):
        if lista[i] % numero == 0:
            list.append(multiplos,lista[i])
            pass
        pass
    return multiplos