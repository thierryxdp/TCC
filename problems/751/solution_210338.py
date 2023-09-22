# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string -> int
def quant_palavras(frase):
    """
    Essa função dado uma string como argumento, irá retornar quantas
    palavras há na string dada
    str->int
    """
    
    variavel = str.count(frase,' ')
    return variavel + 1