def conta_frases (texto):
    '''Entrada: Texto (Variável do tipo string)
       
       Saída: Número de frases no texto de entrada (variável do tipo 
       inteiros)'''
    if '!' or '.' or '...' or '?' in texto:
        return len(texto.split('!')) or len(texto.split('.')) or len(texto.split('...')) or len(texto.split('?'))