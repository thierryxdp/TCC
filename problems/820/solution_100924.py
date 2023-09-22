def posLetra(f,l,n):
    '''Çonta quantas vezes tem uma letra(l) numa frase(f) e caso não tenha o número de vezes
    de um número(n) retorna -1'''
    if f.count(l) < n:
        return -1
    else:
        return f.rindex(l)