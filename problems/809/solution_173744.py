# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
def intercala(l1, l2):
    """Função que dadas duas listas l1 e l2, retorne uma lista l3 que é formada
       intercalandoos elemntos de li e l2.
       list --> listFunção que dadas duas listas l1 e l2, retorne uma lista l3 que é formada
       intercalandoos elemntos de li e l2.
       list --> list"""
    l3 = l1[0:1] + l2[0:1] + l1[1:2] + l2[1:2] + l1[-1:] + l2[-1:]
    return l3