# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string -> int
def quant_palavras(frase):
    """
    Função que calcula quantidade de palavras numa frase
    Parametros: frase
    entrada: str
      saída: int
    """
    a = str.split(frase)
    return len(a)