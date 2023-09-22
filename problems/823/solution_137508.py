def faltante(lista):
    '''retorna o numero da peça que falta dada a lista dos numeros.
    lista->int'''
    i=1
    while i<=len(lista):
        if lista[i-1]==i:
            i+=1
        else:
            return i
   
    return i