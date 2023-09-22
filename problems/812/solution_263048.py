def retira_pontuacao(frase):
    """Função retira a pontuação de uma frase e substitui por
    espaços em branco;
    str -> str"""
    modificacao1 = str.replace(frase,"-"," ") 
    modificacao2 = str.replace(modificacao1,","," ")
    modificacao3 = str.replace(modificacao2,":"," ")
    modificacao4 = str.replace(modificacao3,";"," ")
    modificacao5 = str.replace(modificacao4,"."," ")
    modificacao6 = str.replace(modificacao5,"?"," ")
    modificacao7 = str.replace(modificacao6,"!"," ")
    
    return modificacao7