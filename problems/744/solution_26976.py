# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# str-> str
def hashtag(string):
    return "#"+string[0:(len(string)//2)]+"#"+string[len(string)//2:len(string)]+"#"