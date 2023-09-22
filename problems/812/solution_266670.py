def retira_pontuacao(frase):
    """def que dada uma frase retorna a frase, porém sem os caracteres de pontuacao. str -> str"""
    #_ , ; . , : -
    r1 = str.replace(frase,"_"," ")
    r2 = str.replace(r1,","," ")
    r3 = str.replace(r2,";"," ")
    r4 = str.replace(r3,"."," ")
    r5 = str.replace(r4,","," ")
    r6 = str.replace(r5,":", " ")
    r7 = str.replace(r6,"-"," ")
    return r7