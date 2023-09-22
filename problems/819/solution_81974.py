def filtraMultiplos(lista, numero):
    x = 0
    resultado=[] 
    while x < len(lista):
        if lista[x] % numero== 0:
            list.append(resultado,lista[x])
            x = x+1
            return resultado