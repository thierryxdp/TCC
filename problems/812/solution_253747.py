retira_pontuacao(frase):
    '''
    Retira qualquer tipo de pontuação e substitui por espaço
    
    string -> string
    '''
    pontuacao = [".", ":", ",", ";", "-"]
    
    for i in pontuação:
        if i in frase:
            frase.replace(i, " ")
    
    return frase