def repetidos(l):
    """Dada uma lista "l", retorna o número de vezes que um elemento
    da lista é igual ao elemento anterior
    list -> int """
    i=1
    contador =0
    while i<len(l):
        if l[i]==l[i-1]:
            contador+=1
        i+=1
    return contador