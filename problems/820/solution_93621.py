def posLetra(string,letra,numero):
    '''Função que recebe uma string, uma letra e um número que indica a ocorrência desejada da letra
    e retorna a posição da string que aquela ocorrência da letra está. Caso  exista menos ocorrências da letra do que a ocorrência pedida, a função retorna -1.
    str,str,int->int'''
    p_atual = 0
    quant_encont = 0
    if numero > str.count(frase,letra_desejada):
        return -1
    
    while p_atual < len(frase) and quant_encont < numero:
        letra_atual = frase[p_atual]
        if letra_atual == letra_desejada:
            quant_encont = quant_encont + 1
        p_atual =  p_atual + 1
        
    if quant_encont == numero:
        return p_atual - 1