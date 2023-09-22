# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# str-> str
def hashtag(s):
    """Função que insere o caractere # no inicio, meio e final da string s."""
    s="#"+s[:len(s)//2]+"#"+s[len(s)//2:]+"#"
    return s