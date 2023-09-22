# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# str-> str
def hashtag (string):
    """retorna o # no inicio,meio e fim,  str -> str"""
    metade =len (string)//2
    return "#"+string[:metade]+"#"+string[metade:]+"#"