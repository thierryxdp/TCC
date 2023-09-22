"""Como requerido no exercício, a função conta_frases acaba por contar o número de frases de um texto
a partir das regras de pontuação da língua portuguesa (ponto de exclamação, interrogação, final e reticências).
Porém, as reticências podem ser contadas como um ponto final aplicado três vezes, o que torna necessário
que o número de vezes em que o ponto final apareceu seja subtraído pela quantidade de reticências."""

def conta_frases(frases):
    if str.count(frases, '.')>0:
        return (str.count(frases, '.') - (str.count(frases, '...')%3 + str.count(frases, '...'))) + str.count(frases,'!') + str.count(frases, '?') 
    
    if str.count(frases, '.') == 0:
        return str.count(frases,'?') + str.count(frases, '...') + str.count(frases,'!')