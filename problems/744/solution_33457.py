# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# str-> str
def hashtag(s):
 e=len(s)
    if len(s)%2==0:
        i= s[1:(e/2)]
    
        m= s[(e/2):e]
        
        return i + m