def repetidos(lista):
    '''Função que retorna quantas vezes aparecem números
    repetidos em sequência; recebe como parâmetro uma lista;
    List-->Int'''
    i=0
    repete=0
    while i<len(lista):
        if lista[i]==lista[i+1]:
            repete+=1
        i=i+1
    return repete