def filtraMultiplos(lista,n):
    '''Filtra e retorna os múltiplos, do número n recebido, presentes na lista
    lista, int -> lista'''
    contador = 0
    multiplo = []
    while contador < len(lista):
        if lista[contador] % n == 0:
  		multiplo += lista[contador]
    contador+= 1
    return multiplo