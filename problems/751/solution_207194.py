# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string -> int
def quant_palavras(frase: str) -> int:
    """A função recebe uma frase e retorna o numero de palavras dessa frase
    str -> int"""
    return len(str.split(frase))