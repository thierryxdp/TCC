def faltante(lista):
    ''' Funçao que que retorna um numero 'n' de peças de quebra-cabeças 
    através de uma lista.      list => int '''
    a = 1
    n = len(lista) -1
    while a != len(lista) + 2:
        if a not in lista and a < lista [n]:
            return a
        if a not in lista and a > lista [n]:
            return a
        if a in lista:
            a+=1