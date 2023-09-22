def filtraMultiplos(lista_numeros,numero):
    '''filtra os numeros multiplos de um numero
    list,int --> int'''
    i=0
    multiplos=[]
    while i < len(lista_numeros):
        if lista_numeros[i]%numero==0:
            multiplos=multiplos+lista_numeros[i]
        i=i+1
    return multiplos