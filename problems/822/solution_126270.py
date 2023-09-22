def repetidos(lista):
    """Funçao que dada uma lista de numeros, retorna o numero de vezes que m elemento 
    da lista é igual ao elemento anterior;
    list-->int"""
    i = 0
    cont = 0
    while i<len(lista)-1:
        if(lista[i] == lista[i-1]):
            cont = cont+1
        i = int+1
    return cont