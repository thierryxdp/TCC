def retira_pontuacao(frase):
    """Funcao que dada uma frase, retorna a frase onde todos os caracteres de pontuacao
(incluindo travessao, virgula, dois pontos, ponto e virgula, alem da pontuacao de
encerramento de frase) tanham sido substituidos por espaco; string -> string"""

    frase = str.replace(frase,"—"," ")
    frase = str.replace(frase,"-"," ")
    frase = str.replace(frase,"."," ")
    frase = str.replace(frase,","," ")
    frase = str.replace(frase,":"," ")
    frase = str.replace(frase,";"," ")
    frase = str.replace(frase,"?"," ")
    frase = str.replace(frase,"!"," ")    
    frase = str.replace(frase,"..."," ")
    return frase