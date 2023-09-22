# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# str-> str
def hashtag(s):
    
    m = int(len(s)//2)
    valor_meio = s[m]
    parte1 = s[0:valor_meio]
    parte2 = s[valor_meio::]
    
    a = "#"
    return a + parte1 + a + parte2 + a