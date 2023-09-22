def repetidos(lista):
    """Função que dada uma lista retorna a quantidade de vezes que um elemento é igual ao
    elemento que o precede;
    list -> int"""
    i=0
    c=0
    while i<len(lista):
        if i>0:
            if lista[i] == lista[i-1]:
                c+=1
        i+=1
    return c