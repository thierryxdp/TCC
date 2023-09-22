# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string -> int
def quant_palavras(frase):
    """Funcao que retorna o número de palavras dentro de uma frase
    especificada.
    Entrada: str
    Saida: int
    
    Parameters:
    frase: Frase escolhida para ter suas palavras contadas
    """
    return len(frase.split())