def qtd_divisores(numero):
    '''funcao que retorna a quantidade de
    dividores que um numero tem
    entrada: inteiro
    saida: inteiro 
    '''
    auxiliar= 0
    for divisores in range(1,(numero+1)):
        if numero%divisores==0:
            auxiliar= auxiliar + 1
    return auxiliar