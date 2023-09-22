def retira_pontuacao(frase):
    """Esta é a função que dada uma frase retorma a mesma porém sem os sinais de pontuação, str -> str"""
    frase1= str.replace(frase,","," ")
    frase2= str.replace(frase1,"."," ")
    frase3= str.replace(frase2,"!"," ")
    frase4= str.replace(frase3,"..."," ")
    frase5= str.replace(frase4,".."," ")
    frase6= str.replace(frase5,"?"," ")
    frase7= str.replace(frase6,"-"," ")
    frase8= str.replace(frase7,":"," ")
    frase9= str.replace(frase8,";"," ")
    return frase9