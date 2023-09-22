def freq_palavras(frase):
    '''
Função que recebe uma string e retorna um dicionario 
 onde cada palavra dessa string é uma chave e tem
 como valor o numero de vezes que a palavra aparece.   
    
 str-->dict
    '''

    i=0
    dicio={}
    separar=str.split(frase)
    for freq in separar:
        freq=separar.count(separar[i])
        dicio[separar[i]]=freq
        i=i+1     
    
             
    return dicio