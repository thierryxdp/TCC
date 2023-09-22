# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# str-> str
def hashtag(s):
    #quebrando a string
    esquerda = s[:len(s)//2]
    direita = s[len(s)//2: ]
    
    #alteração
    stringfinal = '#' + esquerda + '#' + direita + '#' 
    
    return stringfinal