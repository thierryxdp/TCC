def retira_pontuacao(frase):
    '''funcao que dada uma frase retorna a frase onde todos os caracteres de ponctuacao tenham sido substituidos por espaco
    str->str'''
    f1=str.replace(frase,','," ")
    f2=str.replace(f1,'-'," ")
    f3=str.replace(f2,':'," ")
    f4=str.replace(f3,';'," ")
    f5=str.replace(f4,'.'," ")
    f6=str.replace(f5,'?'," ")
    f7=str.replace(f6,'!'," ")
    return f7

def inverte(frase):
    '''funcao que dada uma frase de entrada retorna uma outra frase que contenha as mesmas palavras de entrada na ordem inversa
    str->str'''
    minusc=str.lower(frase)
    rempont= retira_pontuacao(minusc)
    lista_frase=str.split(rempont)
    lista_invertida=lista_frase[::-1]
    return lista_invertida