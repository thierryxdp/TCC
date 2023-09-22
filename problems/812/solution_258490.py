def retira_pontuacao(frase):
    """Função que recebe uma frase e retorna a frase sem 
    caracteres de pontuação"""
    str.replace(frase,"."," ")
    str.replace(frase,"!"," ")
    str.replace(frase,"?"," ")
    str.replace(frase,","," ")
    str.replace(frase,":"," ")
    str.replace(frase,";"," ")
    str.replace(frase,"-"," ")
    
    return frase