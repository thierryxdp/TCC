# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# str-> str
def hashtag(s):
    """NNN"""
    metade=len(s)
    meio=s[0:metade]
    inicio_s=s[0:meio]
    fim_s=s[(meio)+(1):-1]
    
    return  '#'+ inicio_s + '#' + fim_s '#'