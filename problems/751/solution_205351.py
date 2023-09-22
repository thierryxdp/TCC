# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string -> int
def quant_palavras(frase):
    """Função que dada uma frase, retorna o número de palavras que ela contém;str->int"""
    y= str.strip(frase)
    return str.count(y,' ')+1