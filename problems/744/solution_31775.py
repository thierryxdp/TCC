# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# str-> str
def hashtag(s):
    """Função que retorna uma nova string com um novo caractere inserido no inicio, meio e fim. Entrada -> str; Saída->str"""
    return return str("#") + str(s)[0:len(s)//2] + str("#") + str(s)[len(s)//2:] + str("#")