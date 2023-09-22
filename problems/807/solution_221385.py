def conta_frases (frase):
    '''
    	essa função conta a quatidade de frases; cada frase é terminada 
        com uma pontuação diferente, sendo essas "!, ?, ..., ."
        str->num
    ''' 
    for x in "!...?.":
        return frase.count(frase, x)