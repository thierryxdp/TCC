# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string -> int
def quant_palavras(frase):
    '''
    função que dada uma frase, retorna o número de palavras da frase;
    str -> int
    '''
    espacos = str.count(frase,' ')
    if str.count(frase, ' ', 0,1) == 0 and str.count(frase, ' ',-1) == 0:
        return espacos + 1
    elif str.count(frase, ' ',0,1) == 1 and str.count(frase, ' ',-1) == 0:
        return espacos
    elif str.count(frase, ' ',0,1) == 0 and str. count(frase, ' ',-1) == 1:
        return espacos
    else:
        return espacos -1