def substitui(s, x, i):
    ''' função que retorna a palavra dada por s substituindo a letra localizada na posição i por uma nova letra dada 'x'; str, str, int -> str'''
     s[i] = x
        return s
        return s[0:i] + x + s[i + 1:]