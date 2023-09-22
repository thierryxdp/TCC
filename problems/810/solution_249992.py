def retira_pontuacao(texto):
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

def inverte (frase):
    """
    Função que dado uma frase retorna uma outra frase
    com as mesmas palavras da incial, mas na ordem inversa,
    sem letras maiuscula e sem pontuações
    string---> string
    """
    f1=str.lower(frase)
    f2=retira_pontuacao(f1)
    return f1[-1:]