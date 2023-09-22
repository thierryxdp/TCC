# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# str-> str
def hashtag(s):
    """NNN"""
    metade= int( len( (s)//2))
    inicio_s=s[0:metade]
    fim_s=s[(metade)+(1):-1]
    
    return  '#'+ inicio_s + '#' + fim_s '#'