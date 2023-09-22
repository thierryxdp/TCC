# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# str-> str
def hashtag(s):
    """A função recebe uma string e retorna ela mesma com o caractere "#"
    inserido no começo, no meio e no final da string
    assinatura:
    str-->str
    casos de teste:
    hashtag ("bit") == #b#it#
    hashtag ("sorrir") == #sor#rir#
    """
    meio = len(s) // 2
    return "#" + str(s[0:meio]) + "#" + str(s[meio:]) + "#"