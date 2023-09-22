def retira_pontuacao(frase):
    '''
    Retira qualquer tipo de pontuação e substitui por espaço
    
    string -> string
    '''
    pontuacao = [".", ":", ",", ";", "-", "!", "?"]
    
    for i in pontuacao:
            frase.replace(i, " ")
    return frase