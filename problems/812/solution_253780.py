def retira_pontuação(frase):
    '''Substitui onde estão os caracteres de pontuação (travessão, vírgula, dois pontos , ponto e vírgula e encerramento de frase) por espaços
    string -> int'''
   	frase=str.replace(frase,","," ")
    frase=str.replace(frase,":"," ")
 	frase=str.replace(frase,"-"," ")
    frase=str.replace(frase,";"," ")
    frase=str.replace(frase,"."," ")
    frase=str.replace(frase,"?"," ")
    frase=str.replace(frase,"!"," ")
    return frase