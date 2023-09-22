def filtra_pares(tupla):
    ''' funcao que recebe uma tupla com 4 elemtros  int como parametro e
    retorna uma tupla apenas com pares''''
    tuplas=()
    if tupla[0]%2==0:
        tuplas = tuplas +(tupla[0],)
    elif tupla[1]%2==0:
        tuplas = tuplas +(tupla[1],)
    elif tupla[2]%2==0:
        tuplas = tuplas +(tupla[2],)
    elif tupla[3]%2==0:
        tuplas = tuplas +(tupla[3],)
        return tuplas
    else:
        return 'Nao existe tuplas com par'