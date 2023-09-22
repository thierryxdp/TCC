def posLetra(frase, letra, n):
    '''Dados uma frase, uma letra e o um número, a função retorna
       em que posição da string aquelaocorrencia de letra esta ou
       -1 caso exista menos ocorrencias do que a pedida
       str, str, int -> int
       Parametros:
       frase: frase a serdigitada
       letra: letra escolhida
       n: número de ocorrencia desejado'''
    i = i2 = 0
    while i < len(frase):
        if frase.count(letra) < n:
            return -1
        if frase[i] == letra:
            i2 += 1
            if i2 == n:
                return i
        i += 1