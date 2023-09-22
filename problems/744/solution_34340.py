# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# str-> str
def hashtag(s):
     '''Função que recebe uma string e insire o caractere "#" no início, no meio
e no final dela. 
str -> tuple'''
        inicio = s[:len(s)//2]
        fim = s[len(s)//2:]
    return "#" + s[:len(s)//2] + "#" + s[len(s)//2:] + "#"