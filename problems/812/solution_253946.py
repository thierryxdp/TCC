def retira_pontuacao(frase):
    """Essa função retira a pontuação da frase. Como entrada temos uma frase 
    e como saída temos a mesma frase sem pontuação;
    str->str"""
    frase1=str.replace(frase,","," ")
    frase2=str.replace(frase1,"."," ")
    frase3=str.replace(frase2,"-"," ")
    frase4=str.replace(frase3,":"," ")
    frase5=str.replace(frase4,";"," ")
    frase6=str.replace(frase5,"!"," ")
    frase7=str.replace(frase6,"?"," ")
    return frase7