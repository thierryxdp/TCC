# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# str-> str
def hashtag(s):
    string=str(s)
    nCaracteres=len(string)
    meioDaString=nCaracteres//2
    return s+string[:meioDaString]+s+[meioDaString+1:]+s