def uppCons (frase):'''Função que recebe uma frase e retorna uma novafrase com
consoante em maíuscula
Entrada(string)
Saída(string)'''
    novafrase =' '
    tamanho = len(frase)
    indice = 0 
    while indice < tamanho:
        if frase[indice] in 'qwrtypsdfghjklzxcvbnmç':
            novafrase += str.upper(frase[indice])
        else: 
            novafrase += frase[indice]
        indice += 1  
    return novafrase