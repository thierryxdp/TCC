# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# str-> str
def hashtag(s):
    """recebe uma string(s) e insere o caractere # no inicio, no meio e no final dela.str-> str"""
    string=str(s)
    meioDaString=len(string)//2
    return "#"+string[:meioDaString]+"#"+string[(meioDaString):]+"#"