def posLetra (string, letra, num):
    '''
       Função que recebe uma frase (string), uma letra 
       (letra) e um numero inteiro (num) e retorna em que
       posição da string a repetição num da letra esta. Caso
       o numero de repetição nn condizer com a quantidade da
       letra na string, a função retornará -1.
       str, str, int -> int
    '''
    qntd_letra = -1
    i = 0
    while i<len(string):
        if letra in string[i]:
            qntd_letra = qntd_letra + 1
        i=i+1
    return qntd_letra