# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string -> int
def quant_palavras(frase):
    """Recebe uma frase e retorna o numero de palavras da frase; str-> int."""
    palavras=list(str.split(frase))
    return len(palavras)