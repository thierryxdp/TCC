def retira_pontuacao(frase) :
    """Retira todos os caracteres de pontuação dada uma frase;
    str -> str"""
    resultado = str.replace(frase,"!"," ")
    resultado += str.replace(frase,"."," ")
    resultado += str.replace(frase,";"," ")
    resultado += str.replace(frase,":"," ")
    resultado += str.replace(frase,","," ")
    resultado += str.replace(frase,"?"," ")
    resultado += str.replace(frase,"-"," ")
    return resultado