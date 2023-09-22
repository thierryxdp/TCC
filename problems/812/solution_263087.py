def retira_pontuacao(frase):
    """função que substitui a pontuação da frase de entrada(str) por espaço e retorna a frase alterada(str)"""
    frase0 =  str.replace(frase,"...",".")
    frase1 =  str.replace(frase0,","," ")
    frase2 =  str.replace(frase1,":"," ")
    frase3 =  str.replace(frase2,";"," ")
    frase4 =  str.replace(frase3,"."," ")
    frase5 =  str.replace(frase4,"!"," ")
    frase6 =  str.replace(frase5,"?"," ")
    frase7 =  str.replace(frase6,"."," ")
    frase8 =  str.replace(frase7,"-"," ")
    return frase8

    
    
    
    
    
    
    
    
    str.replace(frase,"-" and "," and ":" and ";" and "." and "?" and "!", " ")