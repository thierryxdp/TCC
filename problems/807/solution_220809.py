def conta_frase(frase):
    '''conta o numero de frases em um texto sendo que cada 
    frase termina com um ponto final, um ponto de 
    interogaçao, um ponto de exclamaçao ou ou tres pontos em
    sequencia, considerando que nao teremos nenhuma das 
    formas de finalizar seguidas; Ex - ?!'''
    frase=frase.replace('...','.')
    frase=frase.replace('?','.')
    frase=frase.replace('!','.')
    frasesSeparadas=frase.split('.')
    numeroDeFrases=len(frasesSeparadas)
    return numeroDeFrases