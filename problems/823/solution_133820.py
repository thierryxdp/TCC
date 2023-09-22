def faltante(L):
    """Função que dada uma lista de numeros inteiros 
       retorna o numero que está faltando.
       list->int""" 
    i = 0
    numero = 1
    list.sort(L)
    while i < len(L):
        if numero == L[i]:
            numero += 1
        i += 1
    return numero