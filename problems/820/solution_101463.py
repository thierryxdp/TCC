def posLetra (string, letra, num):
    '''
       Função que recebe uma frase (string), uma letra 
       (letra) e um numero inteiro (num) e retorna em que
       posição da string a repetição num da letra esta. Caso
       o numero de repetição nn condizer com a quantidade da
       letra na string, a função retornará -1.
       str, str, int -> int
    '''
    return string.replace(letra,'.',(num-1)).find(letra)