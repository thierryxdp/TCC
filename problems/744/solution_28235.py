# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# str-> str
def hashtag(s):
    "Retorna e insere o caractere '#' no início, no meio e no fim da string. str->str"
    return "#" + s[:len(s)//2] + "#" + s[len(s)//2:] + "#"