# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
def intercala(lista1, lista2):
    '''função que, dadas duas listas ([a,a,a],[b,b,b]), as intercale da
       forma ([a,b,a,b,a,b]). lista, lista -> lista'''
    return [lista1[0]] + [lista2[0]] + [lista1[1]] + [lista2[1]] + [lista1[2]] + [lista2[2]]