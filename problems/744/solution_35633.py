# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# str-> str
def hashtag(s):
    """função que dado um parâmetro s insere o caractere # no início, no meio e no final dela,str->str"""
    caractereNoInicio=[:len(s)//2]
    caractereNoFinal=[len(s)//2:]
    s="#" + caractereNoInicio + "#" + caractereNoFinal +"#"
    return s