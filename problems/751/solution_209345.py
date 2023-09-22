# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string -> int
def quant_palavras(frase):
    """Essa funcao rece como entrada uma frase e retorna o numero de palavras da mesma
    str->int"""
    #frase = str.strip(frase)
    frase = str.split(frase)
    return len(frase)