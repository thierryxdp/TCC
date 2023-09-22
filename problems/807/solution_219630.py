def conta_frases (texto):
    '''Entrada: Texto (Variável do tipo string)
       
       Saída: Número de frases no texto de entrada (variável do tipo 
       inteiros)'''
    return len(texto.split("!" "..." "?" "."))