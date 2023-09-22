def retira_pontuacao(s):
    """retorna a frase de entrada sem sinais de pontuação"""
    s1 = s.replace("-"," ")
    s2 = s1.replace("!","")
    s3 = s2.replace("?"," ")
    s4 = s3.replace(".","")
    s5 = s4.replace(","," ")
    s6 = s5.replace(";"," ")
    s7 = s6.replace(":"," ")
    return s7
def inverte(s):
    """dada uma frase, retorna uma outra frase que contenha as mesmas palavras da
frase de entrada na ordem inversa, sem letras maiúsculas e sem pontuação"""
    s = str.lower(retira_pontuacao(s))
    lista_s = s.split(" ")
    lista_2 = lista_s[::-1]
    string = str.join(" ",lista_2)
    return string