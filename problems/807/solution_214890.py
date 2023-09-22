def conta_frases(texto):
    """Função que recebe um texto e retorna o número de frases dentro dele. str -> int"""
    especias = ['!','?','.']
    texto = texto.split()
    contador = 0
    for laco_palavras in texto:
        for laco_especiais in especias:
            if laco_especiais in laco_palavras:
                contador+=1