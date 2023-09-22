# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string -> int
def quant_palavras(frase):
    """Apos informar uma frasse como parametro de entrada, a funcao retorna quantas palravras a frase tem 
    str -> int"""
    quantidade = str.split(frase)
    return len(quantidade)