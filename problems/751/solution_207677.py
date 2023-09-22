# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string -> int
def quant_palavras(frase):
    """Calcula a quantidade de palavras existentes no parâmetro de entrada 'frase'
    e retorna na saída o número de palavras
    string->int"""
    lista=frase.split()
    return len(lista)