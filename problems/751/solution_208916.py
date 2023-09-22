# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string -> int
def quant_palavras(frase):
    """
    Calcula e retorna o número de palavras de uma frase;
    string -> int
    """
    nova_frase = frase.split(" ")
    return len(nova_frase)