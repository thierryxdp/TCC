# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
def intercala(lista1, lista2):
    """Recebe duas listas com 3 elementos cada, e intercala os elementos da primeira lista com os da segunda lista
    em uma única lista, de forma que apareça um elemento da primeira lista e depois um da segunda, e assim até o fim."""
    
    return [lista1[0] + lista2[0] + lista1[1] + lista2[1] + lista1[2] + lista2[2]]