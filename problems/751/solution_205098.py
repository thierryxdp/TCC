# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string -> int
def quant_palavras(frase):
    """Retorna o número de palavras em uma frase;
    string -> int"""
    if frase[0] == ' ':
        if frase[-1] == ' ':
            return len(str.split(frase, ' '))-2
        else:
            return len(str.split(frase, ' '))-1
    elif frase[-1] == ' ':
        return len(str.split(frase, ' '))-1
    else:
        return len(str.split(frase, ' '))