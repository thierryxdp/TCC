# Posição da letra
def posLetra(frase,letra, n):
    '''Essa função recebe um frase, uma letra e um número, ela
    deve ler a frasde recebida e dizer qual o indice da lera na sua
    enézima ocorrencia de acordo com o numero inteiro inserido;
    STR, STR, INT -> INT'''
    if frase.count(letra) < n:
        return -1
    else:
        i = 0
        t = 1
        while i in range(0, len(frase)):
            if frase[i] == letra:
                if t <= n:
                    pos  = i
                    t += 1
            i += 1
        return pos