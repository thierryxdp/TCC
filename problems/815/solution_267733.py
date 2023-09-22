"""A função insere abaixo utiliza a função sorted para poder que o número indicado pela variável n,
ao ser somado com a lista de números, seja posto de tal forma que a mesma se mantenha crescente.""""

def insere(lista_numeros,n):
    return sorted(lista_numeros + [n])