def retira_pontuacao(frase):
    ''''Dado uma frase, retorna uma frase sem nenhuma pontuação com espaços
    em seu lugar.str -> str'''
    frase = str.replace(frase,"!"," ")
    frase = str.replace(frase,"?"," ")
    frase = str.replace(frase,"..."," ")
    frase = str.replace(frase,"."," ")
    frase = str.replace(frase,"-"," ")
    frase = str.replace(frase,","," ")    
    frase = str.replace(frase,":"," ")
    frase = str.replace(frase,";"," ")  
    return frase