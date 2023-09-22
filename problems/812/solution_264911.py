def retira_pontuacao (frase):
    '''função que substitui pontuações por espaço'''
    if "," is in frase:
        return (frase.replace(","," "))
    
    if "-" is in frase:
        return (frase.replace("."," "))
    
    if ":" is in frase:
        return (frase.replace(":"," "))
    
    if "." is in frase:
        return (frase.replace("."," "))
    
        return frase