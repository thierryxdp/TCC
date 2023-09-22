def faltante(lista):
    copia_lista = lista[:]
    total_pecas = len(copia_lista)+1
    i = 0
    peca = 0
    while copia_lista.index!=copia_lista[i]:
        peca = peca + 1
        i = i+1
    return i