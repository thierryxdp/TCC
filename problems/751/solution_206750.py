# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string -> int
def quant_palavras(frase):
    """Retorna a quantidade de palavras que uma frase contém
    str -> int"""
    
    return str.count(str.split(frase, ' '), ' ')