# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# str-> str
def hashtag(s):
    "dada uma string, insere 3 '#' ao longo dela, uma no início, uma no meio e uma no fim. str ->str"
    return ('#' + s[0:int(len(s)/2)] +'#'+ s[int(len(s)/2):len(s)] + "#")