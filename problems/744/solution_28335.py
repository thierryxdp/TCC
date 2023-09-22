# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# str-> str
def hashtag(s):
    ''' função que coloca um caractere no inicio, meio e fim de uma string
    (s) = string
    saida = string '''
    hastag1 = "#"+ s[0:len(s)//2]+"#"+s[len(s)//2]+"#"
    return hastag1