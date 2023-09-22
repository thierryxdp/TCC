def conta_frases(texto):
    """Função que dado um texo, ira retornar o número de frases contidas no texto.
    casos de teste:
    entrada: "Preciso tirar um cochilo. Meu deus! Que horas são? Vou perder a minha aula..." saida: 4
    entrada: "
    entrada: "
    assinatura: str -> int
    return texto.count("?") + texto.count(".") + texto.count("!") + texto.count("...")