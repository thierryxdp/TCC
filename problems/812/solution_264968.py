def retira_pontuacao(s):
    """Dada uma frase, retorna essa mesma frase
sem a pontuação, incluindo ponto de exclamação, ponto
de interrogação, vírgula, ponto final, travessão, dois
pontos e ponto e vírgula.
assinatura: string --> string
casos de testes:
retira_pontuacao("Preciso tirar um cochilo. Meu Deus! Que horas são? Vou perder minha aula...") == 'Preciso tirar um cochilo  Meu Deus  Que horas são  Vou perder minha aula   '
retira_pontuacao("Python é legal. Dá para fazer muitas coisas...") == 'Python é legal  Dá para fazer muitas coisas   '
retira_pontuacao("Python é legal! Dá para fazer muitas coisas? Ou não?") == 'Python é legal  Dá para fazer muitas coisas  Ou não '
retira_pontuacao("Python é legal? Não sei se da para fazer muitas coisas... Talvez sim.") == 'Python é legal  Não sei se da para fazer muitas coisas    Talvez sim '
"""
    s1 = str.replace(s, "-", " ")
    s2 = str.replace(s1, ",", " ")
    s3 = str.replace(s2, ":", " ")
    s4 = str.replace(s3, ";", " ")
    s5 = str.replace(s4, ".", " ")
    s6 = str.replace(s5, "!", " ")
    s7 = str.replace(s6, "?", " ")
    return s7