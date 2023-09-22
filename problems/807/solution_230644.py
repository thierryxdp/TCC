def conta_frases(frase):
    """Conta o número de frases que aparecem no texto 
    assinatura: str -> int
    testes:
    conta_frases("Bom dia! Como está o tempo hoje?) == 2
    conta_frases("Boa noite! Tudo bem? Que horas são?) == 3
    """
    exclamacao = str.count(frase, "!")
    interrogacao = str.count(frase, "?")
    reticencias = str.count(frase, "...")
    pfinal = str.count(frase, ".") - 3 * reticencias
    return exclamacao + interrogacao + reticencias + pfinal