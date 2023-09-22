def freq_palavras(frases):
    '''funcao que recebe uma string e retorna
    um dicionario com cada palavra da string 
    sendo uma chave e o valor a quantidade de 
    repetição
    entrada: string
    saida: diconario
    '''
    dicionario= {}
    lista_frase= frases.split(' ')
    indice= 0
    
    while indice<len(lista_frase):
        vezes= lista_frase.count((lista_frase[indice]))
        dicionario[(lista_frase[indice])]= int(vezes)
        indice= indice + 1
    
    return dicionario