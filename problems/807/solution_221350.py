#Exercício_02:
''' Essa função recebe um texto e retorna a quantidade de frases que nele há. '''
''' str ---> int. '''

#definindo a string que caragará o texto armazenado:
texto = 'Preciso tirar um cochilo. Meus Deus! Que horas são? Vou perder a minha aula…'

#A função:
def conta_frases(texto_x):
    
    #Computando o número de frases que acabam com ".":
    n_ponto = int(str.count(texto_x, "."))
    
    #Computando o número de frases que acabam com "?":
    n_inte = int(str.count(texto_x, "?"))
    
    #Computando o número de frases que acabam com "!":
    n_excl = int(str.count(texto_x, "!"))
    
    #Computando o número de frases que acabam com "…":
    n_3pontos = int(str.count(texto_x, "…"))
    
    #Calculando o número final de frases:
    número_final_de_frases = n_ponto + n_inte +  n_excl + n_3pontos  
    
    #Retornando:
    return número_final_de_frases

conta_frases(texto)