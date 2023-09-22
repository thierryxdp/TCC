def posLetra (frase,l,p):
    '''função em que dada uma string(frase), uma letra(l) e um número (p) que
    indica a ocorrência desejada da letra (1 para a primeira ocorrência, 2 para
    a segunda, etc) retorne a posição da string em que aquela ocorrência da
    letra está. Caso exista menos ocorrências da letra do que a pedida, a função
    deve retornar '-1';
    str,str,int -> str'''
    o=str.count(frase,l)
    f2=str.replace(frase,l,'.',(p-1))
    if o<p:
        return -1
    else:
        return str.find(f2,l)