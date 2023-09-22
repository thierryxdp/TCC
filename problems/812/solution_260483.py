#Exercício_03:
''' Essa função retira toda pontuação de uma frase e substitui por "espaço". '''
''' str ---> str. '''

def retira_pontuacao(frase):
    
    #Definindo a frase com as mudanças necessárias:
    #Retirando "?":
    frase_final1 = str.replace(frase, "?", " ")
    
    #Retirando "!":
     frase_final2 = str.replace(frase, "!", " ")
        
    #Retirando ",":
     frase_final3 = str.replace(frase, ",", " ")
        
    #Retirando ".":
     frase_final4 = str.replace(frase, ".", " ")
        
    #Retirando "-":
     frase_final5 = str.replace(frase, "-", " ")
        
    #Retirando ":":
     frase_final6 = str.replace(frase, ":", " ")
        
    #Retirando "...":
     frase_final7 = str.replace(frase, "...", " ")
        
    return frase_final7