# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# str-> str
def hashtag(palavra):
    """Função que recebe uma string e insere o caractere '#' no inicio,meio e fim; bool-->bool"""
    meio = len(palavra)//2
    return '#' = palavra[:meio] + '#' + palavra[meio:] + '#'