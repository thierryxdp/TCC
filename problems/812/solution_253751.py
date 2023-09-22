def retira_pontuacao(frase):
    '''
    Retira qualquer tipo de pontuação e substitui por espaço
    
    string -> string
    '''
    pontuacao = [".", ":", ",", ";", "-", "!", "?"]
    
    for i in pontuacao:
        if i in frase:
            print("\n", i)
            frase.replace(i, " ")
    
    return frase