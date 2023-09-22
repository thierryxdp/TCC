# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string -> int
def quant_palavras(frase):
    """conta a quantidade de palavras que existem em determinada frase;
    str->int"""
    x=str.split(frase)
    return len(x)