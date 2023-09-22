# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
def freq_palavras(frases):
    """
    Recebe uma string e retorna um dicionario onde cada palavra
    dessa string e uma chave e tem como valor o numero de vezes que 
    a palavra aparece;
    str -> dict
    """
    dicionario = {}
    palavras = string.split()
    for palavra in palavras:
        dicionario[palavra]=0
    for palavra in palavras:
        quantidade=palavras.count(palavra)
        dicionario[palavra]=quantidade
    return dicionario