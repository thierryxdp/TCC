# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string -> int
def quant_palavras(frase):
    """
    Função que dada uma frase,
    retorna o número de palavras da frase
    Paramêtro de Entrada: string
    Valor de Saida: int
    """
    
    return len(str.split(frase))