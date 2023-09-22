# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string -> int
def quant_palavras(frase):
    """Retorna o número de palavras contidas na frase dada;
       str->int
       Parametro:
       frase: string em formato de frase
    """
    s=str.split(frase)

    return len(s)