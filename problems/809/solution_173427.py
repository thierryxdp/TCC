# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
rom itertools import chain
 
# listas mocks exemplificando o primeiro teste
l1 = ['a', 'b']
l2 = [1, 2]
 
list_comb = list(chain.from_iterable(zip(l1, l2)))
 
assert list_comb == alternate_comb(l1, l2)