# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# str-> str
def hashtag(s):
     """Função que insere o caractere "#" no inicio, no meio e no final da string.
       str -> str."""
        quantidade = len (s)
    return '#' + str (s)[0: quantidade // 2] + '#' + str (s) [quantidade // 2 :] + '#'