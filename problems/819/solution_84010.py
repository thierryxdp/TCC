def filtraMultiplos(lista,divisor):
    tamanho_lista = len(lista)
    chave = []
    contador = 0
    while contador < tamanho_lista :
        if lista[contador]%divisor == 0 :
            chave.append(lista[contador])
        contador = contador + 1
    return chave