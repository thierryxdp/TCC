def posLetra(string,letra,numero):
    '''Função que retorna a posição da string que a ocorrência da letra está
       str,str,int->int'''
    if str.count(string,letra)<numero:
        return -1
    else:
        n=0
        g=0
        while n<len(string):
            n+=1
            if string[n]==letra:
                g+=1
                if g==numero:
                    return n