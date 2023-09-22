def retira_pontuacao(frase):
    frase = temp
    '''
    Retira qualquer tipo de pontuação e substitui por espaço
    
    string -> string
    '''
    pontuacao = [".", ":", ",", ";", "-", "!", "?"]
    
    for i in pontuacao:
        if i in frase:
            temp.replace(i, " ")
    
    return temp