def lingua_p(palavra):
    #define as vogais
    vogal= 'aeiouAEIOU'
    #Variável auxiliar para guardar a string original
    aux=''
    #Percorre cada letra na palavra 
    for letra in palavra:
        #Inclui a consoante na variavel auxiliar
        aux = aux+letra
        #Verifica se a letra é uma vogal
        if letra in vogal:
        #Incluí o P após a vogal com a vogal
        aux=aux+('p'+letra)  
        #Retorna a palavra traduzida em letra minuscula 
        return aux.lower()