# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# str-> str
def hashtag(s):
    """a função recebe uma string s e retorna a string com um # no inicio, no meio e no final dela"""
    string0='#'+str(s)+'#'
    meio=len(string0)//2
    string1=string[0:meio]+'#'+string0[meio:]
    return string1