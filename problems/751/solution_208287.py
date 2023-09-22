#Exercício_01:
''' Essa função recepe uma string e retorna a quantidade
    de palavras que nela há. '''
''' str ---> int. '''

def quant_palavras(frase): 
    
    #Criando uma lista contendo as palavras da frase:
    lista_f = list(str.split(frase))
    
    #Retornando:
    return len(lista_f)