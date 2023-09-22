def conta_frases (texto):
    """funçao que recebe um texto e retorna a quantidade de frases existem no texto com base em que casa frase termina com um ponto (./!/?/...);
entrada: str
saida: int."""

    texto = str.replace (texto, '...', '.')
    final = str.count (texto, '.')
    exclamacao = str.count (texto, '!')
    interrogacao = str.count (texto, '?')

    return final + exclamacao + interrogacao