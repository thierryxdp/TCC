# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# str-> str
def hashtag(s):
    """
    Recebe uma string e a retorna com # no seu inicio, meio e fim
    """
    x = int(len(s)/2)
    s_novo = "#"+s[:x-2]+"#"+s[x:]+"#"
    return s_novo