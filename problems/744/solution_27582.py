# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# str-> str
def hashtag(s):
    """Funcao que recebe uma string e insere o caracter "#" no inicio, meio e fim dela."""
    x = int(len(s)/2)
    
    return "#"+s[0:x]+"#"+s[x:]+"#"