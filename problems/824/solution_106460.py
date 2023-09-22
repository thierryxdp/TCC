def uppCons(frase):
    '''Função que recebe como entrada uma frase e retorna a frase com todas suas consoantes maiúsculas e vogais como estavam na frase original. 
       parâmetro de entrada: str
       valor de retorno: str'''
    contador=0
    novafrase=''
    while contador<len(frase):
        if frase[contador]not in 'AEIOUaeiouãõáéíóúâêîôû' and frase[contador] != frase[0]:
            novafrase= novafrase+ str.upper(frase[contador])
        if frase[contador]in 'AEIOUaeiouãõáéíóúâêîôû' and frase[contador] != frase[0]:
            novafrase= novafrase+ str.lower(frase[contador])
        if frase[contador]== frase [0]:
            novafrase=novafrase+str.upper(frase[contador])
        contador=contador+1
    return novafrase