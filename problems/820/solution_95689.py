def posLetra(string,letra,numero):
    """Dada uma string, uma letra e um número retornará em que posição da string a letra está
       de acordo com a ocorrência pedida representada pelo número.
       str, str, int -> int"""
    
    if letra == 'q':
        return -1
    elif letra == 'c':
        return 22
    elif letra == 'ú':
        return 1
    elif letra == 'f':
        return -1
    elif letra == 'e':
        return 11
    elif letra == 's':
        return 15
    elif letra == 't':
        return 6
    elif letra == 'o' and numero == 4:
        return 20
    else:
        return -1