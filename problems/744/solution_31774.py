# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# str-> str
def hashtag(s):
    """Função que retorna o caracter # no inicio, meio e fim do string"""
    n=(int(s)/2)
    p1=s[:n]
    p2=s[n:]
    return "#"+p1+"#"+p2+"#"