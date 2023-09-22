def posLetra(frase, letra, ocorr):
    '''Função que recebe uma frase, uma letra e um número que indica a ocorrência 
    desejada da letra e retorna em que posição da string aquela ocorrência da letra
    estáinteressante ou -1 caso exista menos ocorrências que o pedido na entrada;
    str, str, int -> int'''
    
    cont = 0
    exist = 0
    pos = 0

    while cont < len(frase) and exist < ocorr:
        if frase[cont] == letra:
            exist +=  1
            pos = cont
            
        cont += 1

    if exist < ocorr:
        return -1
    else:
        return pos