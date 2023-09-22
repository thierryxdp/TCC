# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string -> int
def quant_palavras(frase):
    """Funque retorna apenas a quantidade da frase
    Entrada: str
    Saída: int"""
    frase=frase.split()
    return len(frase)