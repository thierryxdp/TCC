# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string -> int
def quant_palavras(frase):
    """A função calcula e retorna o número de palavras
    da frase escolhida. Considerando a ocorrência de espaços
    no início e no final.
    Entrada: Str
    Saida: Int"""
    return len(str.split(frase, ))