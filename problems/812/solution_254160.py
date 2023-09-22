def retira_pontuacao(frase):
    """Dada uma frase, retorna uma nova frase substituindo as pontuações (-,;:!?) pelo espaço; str -> str"""
    retira1 = str.replace(frase,"-"," ")
    retira2 = str.replace(retira1,","," ")
    retira3 = str.replace(retira2,";"," ")
    retira4 = str.replace(retira3,":"," ")
    retira5 = str.replace(retira4,"!"," ")
    retira6 = str.replace(retira5,"?"," ")
    retira7 = str.replace(retira6,"."," ")
    frase_final = retira7
    return frase_final