# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string -> int
def quant_palavras(frase):
    """Dada uma frase retorna o número de palavras nessa frase
    str=>int"""
 
    return list.count(str.split(frase," "))