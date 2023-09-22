# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# str-> str
def hashtag(s):
    "string--->string"
    "pega uma string do tipo abcd e retorna #ab#cd#"
    sh= "#" + s[:(len(s)//2)] + "#" + s[(len(s))//2:] + "#"
    return sh