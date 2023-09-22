def posLetra(string, l, n):
    
    ''' Função que, dada uma string, uma letra
        e um número que indica a ocorrência desejada
        da letra, retorna em que posição da string
        a ocorrência da letra está; caso exista menos
        ocorrências da letra do que a pedida, função
        retorna -1
        str, str, int -> int '''
    
    nova_string = string.replace(l, '.', n-1)
    
    return nova_string.find(l)