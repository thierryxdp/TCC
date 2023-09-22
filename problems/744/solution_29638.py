# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# str-> str
def hashtag(s):
    """
    Recebe uma string e a retorna com # no seu inicio, meio e fim
    """
    x = int(len(s)/2)
    s_novo = "#"+s[0:x]+"#"+s[x+1:]
    return s_novo