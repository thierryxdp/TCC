# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# str-> str
def hashtag(s):
    '''Entre com uma string cara retornala com '#' no inicio, no meio e no fim
    String -> String'''
    
    n=len(s)
    meio=n//2
    
    return ('#'+s[0:meio]+'#'+s[0:]+s[meio:]+'#')