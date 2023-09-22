# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string -> int
def quant_palavras(frase):
    """funcao que retorna o numero de palavras contidas nas frases indicadas, sendo a entrada frases uma string """
    frase= str.split(frase)
    return len(frase)