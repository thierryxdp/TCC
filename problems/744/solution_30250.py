# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# str-> str
def hashtag(s):
    

    
    p=len(s)
    
    
    g=(p//2)
    
    primeirametade= s[0:g]
    
    segundametade= s[g:]
    
    klebinho = '#'+primeirametade+'#'+segundametade+'#'
    
    return klebinho