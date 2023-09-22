# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# str-> str
def hashtag(s):
    """ Reebe uma string e inseree o caractere "#" no inicio, no meio e no final da string;
    assinatura: str--> str
    testes:
    hashtag('drogaria')=='#drog#aria#'
    hashtag('bit')=='#b#it#'
    hashtag('troçar')== '#tro#çar#'
    """
    s = "#" + s[:len(s)//2]+"#" + s[len(s)//2:]+ "#"
    return s