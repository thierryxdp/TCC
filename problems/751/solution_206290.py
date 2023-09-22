# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string -> int
def quant_palavras(frase):
    """funçao que recebe um frase retorna o numero de palavras que existe nessa frase;
entrada: str;
saida: int."""
    frase = str.split (frase)
    return len (frase)