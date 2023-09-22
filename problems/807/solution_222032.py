#Exercício_02:
''' Essa função recebe um texto e retorna a quantidade de frases que nele há. '''
''' str ---> int. '''

#A função:
def conta_frases(texto_x):
    
    #Computando o número de frases que acabam com ".":
    n_ponto = int(str.count(texto_x, "."))
    
    #Computando o número de frases que acabam com "?":
    n_inte = int(str.count(texto_x, "?"))
    
    #Computando o número de frases que acabam com "!":
    n_excl = int(str.count(texto_x, "!"))
    
    #Computando o número de frases que acabam com "…":
    n_3pontos = int(str.count(texto_x, "..."))
    
    n_3pontos1 = (n_3pontos*3)
    
    #Calculando o número final de frases:
    numero_final_de_frases = n_ponto + n_inte +  n_excl + n_3pontos - n_3pontos1
    
    #Retornando:
    return numero_final_de_frases