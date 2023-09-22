# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string -> int
def quant_palavras(frase):
    """Funçao que retorna  a quantidade de palavras na frase
    entrada:string
    saida:int"""
    if frase[0:1] == " ":
        return len(frase[1:])
    elif frase[-1:-2] == " ":
        return len(frase[0:-1])
    if frase[0:1] == " " and frase[-1:-2] = " ":
        return len(frase) - 2
    else:
        return len(frase)