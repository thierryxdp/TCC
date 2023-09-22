def retira_pontuacao(s):
    cont = 0
    frase_final = " "
    
    while cont < len(s):
        caractere = s[cont]
        
        if caractere in '.,:;-?':
            frase_final = frase_final + " "
            
        else:
            frase_final = frase_final + caractere
        
        cont+=1
        
    return str.lstrip(frase_final)