# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# str-> str
def hashtag(s):
    
    """ Recbe uma string s e coloca o caracter "#" no inicio no meio e no fim
    da string"""
    
    
    s1 = s[:len(s)//2]
    s2 = s[len(s)//2:]
    
    
    return "#" + s1 + "#" + s2 + "#"