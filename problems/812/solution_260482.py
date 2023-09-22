#Exercício_03:
''' Essa função retira toda pontuação de uma frase e substitui por "espaço". '''
''' str ---> str. '''

def retira_pontuacao(frase):
    
    #Definindo a frase com as mudanças necessárias:
    #Retirando "?":
    frase_final = str.replace(frase, "?", " ")
    
    #Retirando "!":
     frase_final = str.replace(frase, "!", " ")
        
    #Retirando ",":
     frase_final = str.replace(frase, ",", " ")
        
    #Retirando ".":
     frase_final = str.replace(frase, ".", " ")
        
    #Retirando "-":
     frase_final = str.replace(frase, "-", " ")
        
    #Retirando ":":
     frase_final = str.replace(frase, ":", " ")
        
    #Retirando "...":
     frase_final = str.replace(frase, "...", " ")
        
    return frase_final