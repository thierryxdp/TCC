# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# str, str -> str
def concatenacao(a, b):
    '''função que dadas duas strings a,b retorna a concatenação delas no formato
        abba
        str,str -> str
    '''
    x= str(a) + str(b) + str(b) + str(a)
    return x