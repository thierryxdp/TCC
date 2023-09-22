# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string -> int
def quant_palavras(frase):
    """Calcula o número de palavras presentes numa dada string"""
    
    espacos = str.split(frase,)

    return len(espacos)