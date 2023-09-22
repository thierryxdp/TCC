# Dada uma lista de peças de 1 a N e tamanho N-1, 
# queremos o número da pecinha faltante.
# Resolução:
# 1. Se a primeira peça não for 1, é esta que falta: devolve-a;
# 2. Se a última peça for o tamanho da lista, a última peça falta;
# 3. Se uma peça i não é igual à antecessora somada em 1,
#    falta a peça i-1.

def faltante(pecinhas: list) -> int:
    '''Dada uma lista de peças de 1 a N e tamanho N-1, 
    devolve o número da pecinha faltante'''
    i = 1
    list.sort(pecinhas)
    if (pecinhas[0] != 1):
        num_pecinha = 1
    elif (pecinhas[-1] == len(pecinhas)):
        num_pecinha = len(pecinhas) + 1
    else:
        while not(pecinhas[i] != pecinhas[i - 1] + 1):
            i += 1
        num_pecinha = pecinhas[i] - 1
    return num_pecinha