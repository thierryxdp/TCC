# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# str-> str
def hashtag(s):
    """Funcao que receba uma string e insira o caractere "#" no inicio, no meio e no final dela,
    str -> str"""
    meio = len(s)//2
    return '#' + s[:meio] + '#' + s[meio:] + '#'