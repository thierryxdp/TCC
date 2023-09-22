# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# str-> str
def hashtag(s):
    """Função que dada uma string, coloca o caractere # no início, no meio e no final dela
assinatura  - str --> str
testes: hashtag("victor") == '#vic#tor#'
hashtag("programação") == '#progr#amação#'
"""
    meio = (len(s)//2)
    return str("#") + s[:meio] + str("#") + s[meio:] + str("#")