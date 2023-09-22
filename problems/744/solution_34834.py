# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# str-> str
"""A função é definida por "s" sendo uma string, a função é executa adiciona "#" no inicio 
da string e depois executa a string até o ponto do meio, depos adicionando "#" no ponto do meio
e continua do ponto do meio da string até o final adicionando "#" no final da string

str-> str """
def hashtag(s):
    return "#"+ s[:len(s)//2] + "#" + s[len(s)//2:] +"#"