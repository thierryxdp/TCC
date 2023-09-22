def retira_pontuacao(frase):
	'''A funcao recebe uma frase e torna a frase onde todos os caracteres de pontuacao
    (travessao, virgula, dois pontos, ponto e virgula e pontuacao de encerramento de
    frase) tenham sido substituidos por espaco.
    Parametro de entrada: str
    Valor de retorno: str'''
    if "—" in frase:
        frase=str.replace(frase,"—"," ")
    if "-" in frase:
        frase=str.replace(frase,"-"," ")
    if "," in frase:
        frase=str.replace(frase,","," ")
    if ":" in frase:
        frase=str.replace(frase,":"," ")
    if ";" in frase:
        frase=str.replace(frase,";"," ")
    if "." in frase:
        frase=str.replace(frase,"."," ")
    if "!" in frase:
        frase=str.replace(frase,"!"," ")
    if "?" in frase:
        frase=str.replace(frase,"?"," ")
    if "..." in frase:
        frase=str.replace(frase,"..."," ")
    return frase