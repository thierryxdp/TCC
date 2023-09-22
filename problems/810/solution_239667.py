def retira_pontuacao(string):
    """ Funcao que retorna a frase com todas as vogais trocadas por i
        string -> string"""
    str1 = str.replace(string,"-"," ")
    str2 = str.replace(str1,","," ")
    str3 = str.replace(str2,":"," ")
    str4 = str.replace(str3,";"," ")
    str5 = str.replace(str4,"."," ")
    str6 = str.replace(str5,"!"," ")
    str7 = str.replace(str6,"?"," ")
    return str7

def inverte(string):
    """ Funcao que retorna a frase inserida invertida e sem pontuação.string -> string"""
    str1 = string.lower(string)
    str2 = retira_pontuacao(str1)
    lista = str.split(str2,)
    list.reverse(lista)
    return str.join(" ",lista)