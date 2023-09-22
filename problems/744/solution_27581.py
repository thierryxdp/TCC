# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# str-> str
def hashtag(s):
    """Funçao que retorna sempre um "#" no inicio no meio e no final de uma string"""
    primeiraParte = str(s[0:len(s)//2])
    segundaParte = str(s[len(s)//2:])
    return '#'+ str(primeiraParte)+ '#'+ str(segundaParte)+ '#'