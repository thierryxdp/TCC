# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# str-> str
def hashtag(s):
    '''função que retorne uma string com caractere (#) no início, no meio e no final dela'''
    inicio = s[:len(s)//2]
    final = s[len(s)//2:]
    s = "#" + inicio + "#" + final + "#"
    s = "#" + s[:len(s)//3] + "#" + s[len(s)//3:] + "#"
    return s