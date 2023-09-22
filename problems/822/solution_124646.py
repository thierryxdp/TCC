# Dada uma lista de números, queremos
# o número de vezes que um elemento da lista
# é igual ao elemento anterior.
# Resolução:
# 1. Se o i-ésimo número for igual ao (i-1)-ésimo, 
#    acrescenta uma repetição às repetições;
# 2. Repete de i = 1 (o 1o elemento não possui antecessor)
#    até i = tamanho da lista menos 1;
# 3. Devolve as repetições.

def repetidos(listnum: list) -> int:
    '''Dada uma lista de números, retorna
    o número de vezes que um elemento da lista
    é igual ao elemento anterior'''
    i = 1
    repeticoes = 0
    while (i < len(listnum)):
        if (listnum[i] == listnum[i - 1]):
            repeticoes += 1
        i += 1
    return repeticoes