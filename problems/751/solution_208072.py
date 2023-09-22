# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string -> int
def quant_palavras(frase):
    """Dada qualquer frase, retornar o número de
       palavras da mesma;
       string -> int"""
    frase = frase.strip( )
    f = frase.split(" ")
    return len (f)