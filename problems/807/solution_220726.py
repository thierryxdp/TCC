def conta_frases(frase):
    frase=frase.replace('...','/')
    frase=frase.replace('?','/')
    frase=frase.replace('.','/')
    frase=frase.replace('!','/')
    frase.split('/')
    return (len(frase.split('/'))-1)
'''funcao que conta o numero de frases em um texto
str->int'''