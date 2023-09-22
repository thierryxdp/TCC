def conta_frases(texto):
    """Recebe um texto e retorna o número de frases
que o mesmo possui através da contagem dos caracteres
que definem o término de uma frase. A lógica considera
que reticências são iguais a três pontos finais juntos
e faz a devida subtração para ajustar à contagem.
str -> int
"""
    contagem_int = str.count(texto,"?")
    contagem_exc = str.count(texto,"!")
    contagem_ret = str.count(texto,"...")
    contagem_pon = str.count(texto,".") - contagem_ret*3
    frases = contagem_int + contagem_exc + contagem_pon + contagem_ret
    return frases