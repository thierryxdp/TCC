# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string -> int
def quant_palavras(frase):
    """Função que retorna o numero x de palavras de um parametro dado
    string -> int"""
    x = len(str.split(frase))
    return x