# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
def intercala(lista1, lista2):
    '''funçao que dadas dua listas L1 e L2 de tamanho 3, gera uma
lista L3 que é formada intercalando os elementos L1 e L2.
list -> list'''
    L3=lista1+lista2
    L3[::2]=lista1
    L3[1::2]=lista2
    return L3