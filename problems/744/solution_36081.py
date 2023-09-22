# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# str-> str
def hashtag(s):
    string=str(s)
    meioDaString=len(string)//2
    return "#"+string[:meioDaString]