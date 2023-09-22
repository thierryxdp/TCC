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
    '''
    Dada uma frase, remove-se seus pontos e todas palavras ficam minusculas,
    em seguida a ordem das palavras é invertida.
    
    string -> string
    '''
    frase = retira_pontuacao(frase).lower() #Retira pontuacao e coloca em minusculo
    frase = frase.split()                   #Divide a string
    frase = str.join(' ', frase[::-1])     #Inverte a lista e a junta os elementos em uma string na ordem invertida/
    return frase