def retira_pontuacao(frase):
    '''
    Retira qualquer tipo de pontuação e substitui por espaço
    
    string -> string
    '''
    pontuacao = [".", ":", ",", ";", "-", "!", "?"]
    
    for i in pontuacao:
        if i in frase:
            frase = frase.replace(i, " ")
            
    return frase

def inverte(frase):
    frase = retira_pontuacao(frase).lower()
    frase = frase.split()
    frase = str.join(' ', frase[::-1])
    return frase