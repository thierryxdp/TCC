# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# str-> str
def hashtag(s):
    #A função recebe uma palavra e coloca um "#" no início, no meio e final dela
    m = len(s)//2
    return "#" + s[:m] + "#" + s[m:]