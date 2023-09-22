def insere(lista_numero,n):
    for fim in range(len(L)-1, 0, -1):
        imax = indice_maior(lista_numero, fim)
        troca(lista_numero, imax, fim)