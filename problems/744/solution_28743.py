# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# str-> str
def hashtag(s):
    """
    
    
    """
    string_hashtag=''
    
    meio=s[:len(s)//2]
    
    s_comeco=s[:meio]
    s_fim=s[meio:]
    string_hashtag=string_hastag+'#'+s_comeco+'#'+s_fim+'#'
    
    return string_hashtag