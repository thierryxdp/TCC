def conta_frases(texto):
    """Função que recebe um texto e retorna a quatidade de frases
       Parametros: string -> int"""
    esp = ['?','!','.']
    texto = texto.split()
    contador = 0
    for palavras in texto:
        for especiais in esp:
            if especiais in palavras:
                contador += 1
    return contador