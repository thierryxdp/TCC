# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
def intercala(lista1, lista2):
    '''Recebe duas listas de tamanho 3 e gera uma nova lista intercalando os elementos das listas passadas.
    lista, lista -> lista'''

    es1 = lista1
    es2 = lista2

    a = es1[0]
    b = es2[0]
    c = es1[1]
    d = es2[1]
    e = es1[2]
    f = es2[2]

    return [a, b, c, d, e, f]