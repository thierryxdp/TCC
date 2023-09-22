def filtra_pares(tupla):
    '''funcao que, dada uma tupla de 4 inteiros, retorna outra tupla apenas com os inteiros
    pares; tuple->tuple'''
    num_pares=()
    if tupla[0]%2==0:
        num_pares=num_pares+(tupla[0],)
    if tupla[1]%2==0:
        num_pares=num_pares+(tupla[1],)
    if tupla[2]%2==0:
        num_pares=num_pares+(tupla[2],)
    if tupla[3]%2==0:
        num_pares=num_pares+(tupla[3],)
    return num_pares