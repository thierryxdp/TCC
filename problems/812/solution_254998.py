def retira_pontuacao(frase):
    """funçao que dada uma frase,retorna a frase onde todods os caracteres de pontuacao foram substituidos; str->str"""
    frase=str.replace(frase,","," ")
    frase=str.replace(frase,":"," ")
    frase=str.replace(frase,";"," ")
    frase=str.replace(frase,"!"," ")
    frase=str.replace(frase,"?"," ") 
    frase=str.replace(frase,"/"," ")
    frase=str.replace(frase,"-"," ")
    return str.replace(frase,"."," ")