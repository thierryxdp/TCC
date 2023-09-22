def retira_pontuacao(frase):
    """Função que recebe uma frase e retorna a frase sem 
    caracteres de pontuação"""
   	if . in frase:
        str.replace(frase,"."," ")
    if ! in frase:
        str.replace(frase,"!"," ")
    if ? in frase:
        str.replace(frase,"?"," ")
    if , in frase:
        str.replace(frase,","," ")
    if : in frase:
        str.replace(frase,":"," ")
    if ; in frase:
        str.replace(frase,";"," ")
    if - in frase:
        str.replace(frase,"-"," ")
        return frase