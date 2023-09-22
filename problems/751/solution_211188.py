# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string -> int
def quant_palavras(frase):
    """Recebe uma string, divimos essa string e contamos quantos elemntos se formaram
    str-->int
    """
    
    r = frase.split()
    l = len(r)
    return l