# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string -> int
def quant_palavras(frase):
    """Coloque uma frase do tipo string e o valor retornado será a quantidade de palavras do mesmo"""
    frase1=frase.strip()
    frase2=frase1.split(" ")
    frase3=len(frase2)
    return frase3