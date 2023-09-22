def retira_pontuacao(frase):
    "função que, dado uma frase, retorna esta frase com todos os caracteres de pontuação removidos e substituídos por espaço." 
    frase = str.replace(frase,"-"," ")
    frase = str.replace(frase,","," ")
    frase = str.replace(frase,":"," ")
    frase = str.replace(frase,";"," ")
    frase = str.replace(frase,"."," ")
    frase = str.replace(frase,"!"," ")
    frase = str.replace(frase,"?"," ")
    return frase