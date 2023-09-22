def uppCons(frase):
    '''Função retorna dada frase com todas as consoantes maiúsculas;
    str -> str'''
    lista=list(frase)
    indice=0
    while indice<len(lista):
        if lista[indice] in 'bcdfghjklmnpqrstvxwyz':
            lista[indice]=str.upper(lista[indice])
        indice +=1    
    frase=''.join(lista)
    return frase