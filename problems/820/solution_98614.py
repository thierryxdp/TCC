def posLetra(frase,letra,indice):
    '''Dada uma frase, letra e a ocorrencia desejada dessa 
    letra na frase, retorna a posição na frase onde essa
    ocorrência está. Caso exista menos ocorrências da letra
    do que a passada como parâmetro, retorna -1;
    str, str, int --> int'''
    if str.count(frase,letra) >= indice:
        frase = str.replace(frase,letra,'4',indice - 1)
        return str.index(frase,letra)
    else:
        return -1