# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# str-> str
def hashtag(s):
    if len(str(s))//2==0:
        return '#' + str(s)[0:len(s)//2] + '#' + str(s)[len(s)//2:] + '#'
    else:
        return '#' + str(s)[0:len(s)//2]+ '#' + str(s)[len(s)//2:] + '#'