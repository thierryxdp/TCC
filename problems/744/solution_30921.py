# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# str-> str
def hashtag(s):
    """Dada uma palavra s, a função insere um hashtag no início, no meio e no fim da palavra. Recebe valores do tipo string e retorna um valor string."""
    quantidade_caracteres = len(s)
    metade_das_quantidades = int(quantidade_caracteres/2)
    return "#" + s[0:metade_das_quantidades] + "#" + s[metade_das_quantidades:] + "#"