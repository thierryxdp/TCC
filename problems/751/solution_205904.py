# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string -> int
def quant_palavras(frase):
    """Função que retorna o número de palavras da frase
        str-> int"""
        frase1 = frase.split()
        return len(frase1)