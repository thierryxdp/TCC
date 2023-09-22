def inverte(f):
    """
    Função que dada uma frase retorne uma outra frase que contenha
    as mesmas palavras da frase de entrada na ordem inversa, sem
    letras maiúsculas, e sem a pontuação.
    Parametro de entrada: String
    Valor de saida: String
    """
    retira = str.strip(f, "-")
    retira1=str.replace(retira,   "!"," ")
    retira2=str.replace(retira1,  "?"," ")
    retira3=str.replace(retira2,  "."," ")
    retira4=str.replace(retira3,  "/"," ")
    retira5=str.replace(retira4,  ":"," ")
    retira6=str.replace(retira5,  ";"," ")
    retira7=str.replace(retira6,  "-"," ")
    retira8=str.replace(retira7,  ","," ")
    virar_list=str.split(retira8)
    invertido=virar_list[::-1]
    virar_string=str.join(" ",invertido)
    minuscula=str.lower(virar_string)
    
    frase_invertida=minuscula
    return frase_invertida