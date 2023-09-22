# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# str, str -> str
def concatenacao(a, b):
    ''' Recebe as strings "a" e "b" e retorna a concatenação
    delas no formato abba'''
    ''' str, str -> str'''
    #Casos de teste:
    '''concatenacao('Luiz','Felipe')
    LuizFelipeFelipeLuiz
    concatenacao('informática','computacao')
    informaticacomputacaocomputacaoinformatica
    concatenacao('quimica','curso')
    quimicacursocursoquimica'''
    return (str(a) + str(b) + str(b) + str(a))