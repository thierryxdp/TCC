def retira_pontuacao(frase):
    """Funcao que dada uma frase, retorne a frase onde todos os caracteres de pontuação(incluindo travessão, vírgula, dois pontos, ponto e vírgula, além da pontuação de encerramento de frase) tenham sido substituídos por espaço.
    string -> string"""
    filtro1 = str.replace(frase,'-',' ')
    filtro2 = str.replace(filtro1,',',' ')
    filtro3 = str.replace(filtro2,':',' ')
    filtro4 = str.replace(filtro3,';',' ')
    filtro5 = str.replace(filtro4,'!',' ')
    filtro6 = str.replace(filtro5,'.',' ')
    filtro7 = str.replace(filtro6,'?',' ')
    
    return filtro7