# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# str-> str
def hashtag(s):
    """Informada a string a função retorna a string adicionando 
    hashtag no inicio, meio e final da mesma."""
    y=(s)[:1]+'#'+(s)[1:]
    return '',join('#',(y),'#')