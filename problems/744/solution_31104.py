# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# str-> str
def hashtag(s):
    "Insira # no inicio, meio e fim de uma dada string"
    s= "#"+s[:len(s)//2]+"#"+s[len(s)//2:]+"#"
    return s