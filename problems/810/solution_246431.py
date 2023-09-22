def retira_pontuacao(frase):
    """retira a pontuação de uma frase;
str -> str"""
    modificacao1 = str.replace(frase,"-"," ") 
    modificacao2 = str.replace(modificacao1,","," ")
    modificacao3 = str.replace(modificacao2,":"," ")
    modificacao4 = str.replace(modificacao3,";"," ")
    modificacao5 = str.replace(modificacao4,"."," ")
    modificacao6 = str.replace(modificacao5,"?"," ")
    modificacao7 = str.replace(modificacao6,"!"," ")
    
    return modificacao7

def inverte(frase):
    """Retorna uma frase na ordem inversa, sem pontuação
    ou letras maiúsculas;
    str -> str"""
    frase = retira_pontuacao(frase)
    frase = str.lower(frase)
    frase = str.split(frase)
    list.reverse(frase)
    frase_inversa = str.join(" ",frase)
    return frase_inversa