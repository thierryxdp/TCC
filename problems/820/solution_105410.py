def posLetra(texto,letra,numero=0):
    '''recebe uma duas strings, sendo a primeira um texto e a segunda uma letra, junto com
    um numero, retornando o indice da ocorrencia indicada pelo numero da letra no texto
    retornando -1 se a letra nao for encontrada ou o numero for maior que a quantidade de
    ocorrencias da letra no texto
    str,str,int -> int'''
    x = 0
    indice = str.find(texto,letra)
    if indice == -1:
        return indice
    x = 1
    while x < numero:
        indice = str.find(texto,letra,indice+1)
        if indice == -1:
        	return indice
        x=x+1
    return indice