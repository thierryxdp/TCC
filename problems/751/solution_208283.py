# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string -> int
def quant_palavras(frase):
    """Função que descobre quantas palavras possui uma frase"""
    frase_separada= str.split(frase)
    numero_de_palavras= len(frase_separada)
    return numero_de_palavras