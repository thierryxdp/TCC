def repetidos(lista):
    """Função que dada uma lista de números, retorna o
       número de vezes que um elemento da lista é 
       igual ao elemento anterior.
       lista->int"""
    numeros = 0
    i = 0
    while i < len(lista):
        if [i] == [i+1]:
            numeros += lista[i]
        i = i + 1
    return numeros