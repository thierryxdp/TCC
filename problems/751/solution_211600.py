# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string -> int
def quant_palavras(frase):
    """ Retorna o número de palavras contidas na frase de entrada 
    entra -> string 
    saída -> string"""
    quantidade = str.split(frase)
    return len(quantidade)