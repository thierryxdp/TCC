def conta_frases(texto):
    ''' Função que dada uma string (texto) que represente um texto, 
    retorna o número de frases que tal texto possui considerando os
    caracteres ponto (.), exclamação (!), interrogação (?) e reticências
    (...) como sendo a separação de cada frase.
    Entrada: str
    Retorno: int '''
    
    numero_caracteres = str.count(texto,".")+str.count(texto,"...")+str.count(texto,"!")+str.count(texto,"?")
    
    return numero_caracteres