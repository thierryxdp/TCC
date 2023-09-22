def insere(lista,n):
    l=lista.sort(reverse=False)
    return l[:n]+ n +l[n:]