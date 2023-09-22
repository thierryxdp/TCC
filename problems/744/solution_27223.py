# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# str-> str
def hashtag(s):
    
    # Calculo a posição do meio da string
    p = int(len(s)/2)
    
    # Coloco as hashtags no início meio e final,
    # Fatiando a string nesses locais
    return '#' + s[0:p] + '#' + s[p:] + '#'