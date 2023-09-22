def conta_frases(texto):
    ''' Função que dada uma string (texto) que represente um texto, 
    retorna o número de frases que tal texto possui considerando os
    caracteres ponto (.), exclamação (!), interrogação (?) e reticências
    (...) como sendo a separação de cada frase.
    Entrada: str
    Retorno: int '''
    
    frase1 = str.split(texto,"!")
    frase2 = str.split(texto,"?")
    frase3 = str.split(texto,"...")
    frase4 = str.split(texto,".")

    numero_frases = len(frase1+frase2+frase3+frase4)

    return numero_frases