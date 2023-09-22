# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# str-> str
def hashtag(s):
    string = s
    dividir = len(string)//2
    hastag = '#'
    return hastag+string[0:dividir]+hastag+string[dividir:]+hastag