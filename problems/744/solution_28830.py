# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# str-> str
def hashtag(s):
    
    
    metade=len(s)//2
    resultado="#"+s[0:metade]+"#"+s[metade:len(s)]+"#"
    
    return resultado