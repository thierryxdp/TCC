# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string -> int
def quant_palavras(frase):
    """Funcao que indica a quantidade de palavras em uma frase dada"""
    substituicao = str.replace(str.strip(frase),' ', '&@')
    contagem = str.count(substituicao,'&@')+1
    return contagem