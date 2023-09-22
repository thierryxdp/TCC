def repetidos(listaR):
    "retorna o número de vezes ocorre que um elemneto da lista é igual ao anterior"
    cont = 0
    j = 1
    while j < len(listaR):
        if listaR[j] == (listaR[j-1]):
            listaR.count(listaR[j])
            cont += 1
        j += 1
    return cont