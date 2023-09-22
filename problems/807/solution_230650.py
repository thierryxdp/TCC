def conta_frases(nfrases):
    """Conta o número de frases que aparecem no texto.
Assinatura: str -> int
Casos de teste:
("Preciso tirar um cochilo. Meu Deus! Que horas são? Vou perder a minha aula...") == 4
("Gol! Ah, não... Sério? Não acredito que o juiz marcou impedimento. Comprado.") == 5
"""
    num_exc = str.count(nfrases, "!")
    num_int = str.count(nfrases, "?")
    num_ret = str.count(nfrases, "...")
    num_dot = str.count(nfrases,".") - 3*(str.count(nfrases,"..."))
    num_frases = num_exc + num_int + num_ret + num_dot
    return num_frases