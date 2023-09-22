# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# str-> str
def hashtag(s):
    "dado uma string,sera retornado '#' no inicio, no meio e no fim dela"
    meio=len(s)//2
    inicio=s[:meio]
    fim=s[meio:]
    return "#"+inicio+"#"+fim+"#"