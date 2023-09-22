# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# str-> str
def hashtag(s):
    """Função que dada uma string, coloca o caractere # no início, no meio e no final dela
assinatura  - str --> str
"""
    meio = (len(S)//2)
    string_alterada3 = str("#") + s[:meio] + str("#") + s[meio:] + str("#")
    return string_alterada3