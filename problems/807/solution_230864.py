def conta_frases(texto):
    """Função que dado um texo, ira retornar o número de frases contidas no texto.
    casos de teste:
    entrada: "Preciso tirar um cochilo. Meu deus! Que horas são? Vou perder a minha aula..." saida: 4
    entrada: "Em dezembro de 81..." saida: 1 
    entrada: "Nossa! Que casa bonita." saida: 2
    assinatura: str -> int"""
    A = "..."
    return texto.count("?") + A + texto.count("!") + texto.count(".")