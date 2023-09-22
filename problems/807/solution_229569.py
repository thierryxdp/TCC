def conta_frases(s):
    """Retorna o número de frases que
aparecem no dado texto.
OBS: Cada frase do texto é terminada com
ponto final, um ponto de exclamação, um ponto de
interrogação ou reticências. 
assinatura: string --> int
casos de testes:
conta_frases("Preciso tirar um cochilo. Meu Deus! Que horas são? Vou perder minha aula...")== 4
conta_frases("Python é legal. Dá para fazer muitas coisas...") == 2
conta_frases("Python é legal! Dá para fazer muitas coisas? Ou não?") == 3
conta_frases("Python é legal? Não sei se da para fazer muitas coisas... Talvez sim.") == 3
"""
    s1 = str.count(s, "...")
    s_depois_das_reticencias = str.replace(s, "...", "XXX")
    s2 = s_depois_das_reticencias
    s3 = str.count(s2, ".")
    s4 = str.count(s2, "!")
    s5 = str.count(s2, "?")
    return s1 + s3 + s4 + s5