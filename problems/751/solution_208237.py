# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string -> int
def quant_palavras(frase):
    """dada uma frase com espaço entre suas palavras,retorna quantas palavras essa frase tem
    str-->int"""
    palavras=str.split(frase)
    return len(palavras)