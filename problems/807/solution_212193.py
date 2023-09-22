def conta_frases(texto):
    ''' Dado um texto como entrada (entre aspas simples ou duplas), a funcao
    retorna a quantidade de frases que ele possui. As frases sao separadas por
    pontos finais, interrogacao, exclamacao ou reticencias. Pontos exclamati-
    vos e interrogativos devem aparecer sozinhos, com apenas um de cada para 
    terminar a frase correspondente (um '!' para terminar uma exclamacao e um
    '?' para terminar uma pergunta);
    str -> int '''
    
    texto = texto.replace('!','*')
    texto = texto.replace('?','*')
    texto = texto.replace('...','*')
    texto = texto.replace('.','*')
    
    return texto.count('*')