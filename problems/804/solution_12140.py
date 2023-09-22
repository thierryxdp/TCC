def filtra_pares(tupla):
    '''funcao que recebe uma tupla com quatro elementos
    inteiros como parametros e retorne uma nova tupla
    contendo apenas os elementos pares da tupla original
    na mesma ordem
    tuple->tuple'''
    tuplavazia=()
    if tupla[0]%==0:
        tuplavazia= tuplavazia + (tupla[0],)
        if tupla[1]%==0:
            tuplavazia= tuplavazia + (tupla[1],)
            if tupla[2]%==0:
                tuplavazia= tuplavazia + (tupla[2],)
                if tupla[3]%==0:
                    tuplavazia= tuplavazia + (tupla[3],)
                    return tuplavazia