# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string -> int
def quant_palavras(frase):
    """Retorna a quantidade de palavras que há numa frase; String;String->int"""
    separacao=frase.split()
    return len(separacao)