# função posLetra

def posLetra(string, letra, n):
    '''Dada uma string, uma letra e um número que indique a ocorrencia desejada da letra, retorna 
    a posição da string que aquela ocorrencia da letra está.
    str, str, int -> int'''
    i=0
    if string.count(letra) < n:
                return -1
    while i < len(string):
        if string[i] == letra and string[:i+1].count(letra) == n:
            return i
        i+=1