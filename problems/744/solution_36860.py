# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# str-> str
def hashtag (string):
    """dado uma string, retorna essa string com uma hashtag no inicio, no meio e no final. parametro: string --> #str#ing#"""
    fatiamento1 = "#" + string[0:len(string)//2] + "#"
    frase_final = fatiamento1 + string[len(string)//2:len(string)] + "#"
    return frase_final