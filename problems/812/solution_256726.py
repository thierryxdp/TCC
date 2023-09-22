def retira_pontuacao(frase):
    """Dada uma frase, retorna a mesma substituindo os caracteres de pontuacao por espaco branco"""
    """entrada: str
    saida: str"""
    
    a = str.replace(frase,"-"," ")
    b = str.replace(frase,","," ")
    c = str.replace(frase,":"," ")
    d = str.replace(frase,";"," ")
    e = str.replace(frase,"!"," ")
    f = str.replace(frase,"?"," ")
    g = str.replace(frase,"."," ")
    
    return a+b+c+d+e+f+g