# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# str-> str
def hashtag(s):
    "Função na qual insere o carectere # no inicio, meio, e fim de uma string"
    comp=len(s)
    return '#' + s[0:int(comp/2)] + '#' + s[int(comp/2):] + '#'