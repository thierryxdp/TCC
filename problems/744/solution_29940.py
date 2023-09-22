# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# str-> str
def hashtag(s):
    '''Função que insere o caractere "#" no início, meio e fim
    da string "s" de entrada'''
    '''str -> str'''
    #Casos de teste:
    '''hashtag('Felipe') -> #Fel#ipe#
       hashtag('Flamengo')->#Flam#engo#
       hastag ('Informática')->#Infor#mática#'''
    s = "#" + s[:len(s)//2] + "#" + s[len(s)//2:]+ "#"
    return s