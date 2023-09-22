def filtraMultiplos(lista, numero):
    '''funcao que calcula os multiplos de um
    numero dado como parametro
    entrada: lista, inteiro
    saida: lista
    '''
    indice= 0
    multiplos= ()
    while lista[indice]%numero==0:
        multiplos= multiplos + (lista[indice])
        indice= indice+1
    return multiplos