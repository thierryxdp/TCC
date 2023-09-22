# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string -> int
def quant_palavras(frase):
    """função retorna o numero de palavras numa frase
       primeiro tira(cria uma nova) os espaços em branco do lado da fras
       str ---- > int
    """
    frase = str.strip(frase)
    return str.count(frase,' ') + 1