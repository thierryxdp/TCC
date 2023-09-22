# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
def intercala(lista1, lista2):
    ''' funcao que junta duas listas '''
    ''' int -> int '''
    return [*sum(zip(lista1,lista2),())]