# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# str, str -> str
def concatenacao(a, b):
    '''str, str -> str 
    retorna uma string na forma a+b+b+a''' 
    ab= a+b 
    ba= b+a 
    return ab+ba