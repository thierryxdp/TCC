# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# str-> str
def hashtag(s):
    
    if len(s) % 2 == 0:
       a = len(s)
       a = a / 2
       string1 = s [:a:]
       string2 = s [a+1:-1:]
       return '#' +string1 + '#' + string2 + '#'