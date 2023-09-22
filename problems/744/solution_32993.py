# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# str-> str
def hashtag(s):
    '''Função que insere o caractere "#" no início, meio e final de uma string fornecida pelo usuário;
    str -> str'''
    meio = len(s)%2
    if meio == 0:
        return "#" + s[0:meio] + "#" + str[meio:len(s)]
    else:
        return "#" + s[0:meio+1] + "#" + str[meio+1:len(s)]