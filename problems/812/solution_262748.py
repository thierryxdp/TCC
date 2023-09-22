def retira_pontuacao(frase):
    '''Dada uma frase, retorna essa mesma rase, só que com os caracteres de pontuação substituídos por espaço; str -> str'''

    texto = str.replace(texto,"."," ")
    texto = str.replace(texto,"?"," ")
    texto = str.replace(texto,"!"," ")
    
    texto = str.replace(texto,","," ")
    texto = str.replace(texto,";"," ")
    
    texto = str.replace(texto,"-"," ")
    texto = str.replace(texto,":"," ")
    
    texto = str.replace(texto,"..."," ")
    
    return texto