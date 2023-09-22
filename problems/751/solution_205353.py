# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string -> int
def quant_palavras(frase):
    """Verifica e retorna a quantidade de palavras contidas em uma frase;
    str->int"""
    qntd_palavras=str.split(frase," ")
    return len(qntd_palavras)