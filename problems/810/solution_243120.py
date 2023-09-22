def inverte(texto):
    ''' função que retira pontuações, letras maiusculas e inverte a ordem das palavras numa frase em String
    String -> String'''
    texto = str.replace(texto, "-"," ")
    texto = str.replace(texto, ","," ")
    texto = str.replace(texto, ":"," ")
    texto = str.replace(texto, ";"," ")
    texto = str.replace(texto, "."," ")
    texto = str.replace(texto, "?"," ")
    texto = str.replace(texto, "!"," ")
    texto = str.replace(texto, "..."," ")
    texto = str.lower(texto)
    
    
    lista = str.split(texto)
    
    
    
    return str.join(" ",lista[::-1])