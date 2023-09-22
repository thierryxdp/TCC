def retira_pontuacao(frase):
    """Dada uma frase, retorna a mesma frase sem os caracteres de pontuacao"""
    """entrada: str
    saida:str"""
    
    frase = str.replace(frase,"-"," ")
    frase = str.replace(frase,","," ")
    frase = str.replace(frase,":"," ")
    frase = str.replace(frase,";"," ")
    frase = str.replace(frase,"."," ")
    frase = str.replace(frase,"!"," ")
    frase = str.replace(frase,"?"," ")
    
    return frase