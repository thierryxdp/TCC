def posLetra(string, letra, numero):
    '''funcao que retorna a posicao de uma 
    letra, em uma frase, dada um numero de
    ocorrencia
    entrada: string, string, inteiro
    saida: inteiro
    '''
    indice=0 
    numero_ocorrencias= []
    while indice<len(string):
        if string[indice]==letra:
            numero_ocorrencias.append(indice)
        indice= indice+ 1
    if numero>len(numero_ocorrencias):
        return -1
    if numero<=len(numero_ocorrencias):
        return numero_ocorrencias[(numero-1)]