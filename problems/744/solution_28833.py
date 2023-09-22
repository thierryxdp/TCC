# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# str-> str
def hashtag(s):
    word1=s[:len(s)//2]
    word2=s[len(s)//2+1:]
    return "#"+word1+"#"+word2+"#"