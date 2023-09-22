# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string -> int
def quant_palavras(frase):
    """Função retorna o número de palavras da frase;
    string -> int """
    palavras = str.split(frase)
    return len (palavras)