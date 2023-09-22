def faltante(lista):
    list.sort(lista)
    proximo = 0 
    peca = 0
    while proximo <len(lista) and peca < len(lista):
        if lista [proximo] - lista[peca] == -2:
            return lista[proximo] + 1
    	proximo = proximo + 1
    	peca = peca + 1
    if lista [0] == 2:
        return 1
    else: 
        return lista[proximo]+1