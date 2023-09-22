# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
def intercala(lista1, lista2):
    '''Função recebe duas listas com a mesma quantidade de elementos
    e returna uma lista com tais elementos intercalados'''
    return [*sum(zip(lista1,lista2),())]