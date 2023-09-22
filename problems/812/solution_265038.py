def retira_pontuacao(frase):
    """
    Função que dado um texto retorna o mesmo com os
    caracteres de pontuação substituidos por espaços
    str--->str
    """
    t1=str.replace(frase,"-"," ")
    t2=str.replace(t1,","," ")
    t3=str.replace(t2,";"," ")
    t4=str.replace(t3,":"," ")
    t5=str.replace(t4,"."," ")
    t6=str.replace(t5,"!"," ")
    t7=str.replace(t6,"?"," ")
    return t7