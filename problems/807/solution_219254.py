def conta_frases(texto):
    ''' Função que dada uma string (texto) que represente um texto, 
    retorna o número de frases que tal texto possui considerando os
    caracteres ponto (.), exclamação (!), interrogação (?) e reticências
    (...) como sendo a separação de cada frase.
    Entrada: str
    Retorno: int '''
    
    frase1 = str.count(texto,"!")
    frase2 = str.count(texto,"?")
    frase3 = str.count(texto,"...")
    frase4 = str.count(texto,".")

    numero_caracteres = frase1 + frase2 + frase3 + frase4
    numero_frases = len(numero_caracteres)