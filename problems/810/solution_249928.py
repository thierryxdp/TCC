def retira_pontuacao(s):
    s1 = str.replace(s, "-", " ")
    s2 = str.replace(s1, ",", " ")
    s3 = str.replace(s2, ":", " ")
    s4 = str.replace(s3, ";", " ")
    s5 = str.replace(s4, ".", " ")
    s6 = str.replace(s5, "!", " ")
    s7 = str.replace(s6, "?", " ")
    return s7

def inverte(s):
    """Dada uma frase, retorna uma outra frase
com as mesmas palavras da frase de entrada mas na ordem
inversa, sem letras maiúsculas e sem pontuação.
assinatura: string --> string
casos de teste:
inverte("Nossa, como eu gosto de chocolate.") == 'chocolate de gosto eu como nossa'
inverte("Preciso tirar um cochilo. Meu Deus! Que horas são? Vou perder minha aula...") == 'aula minha perder vou são horas que deus meu cochilo um tirar preciso'
inverte("Python é legal! Dá para fazer muitas coisas? Ou não?") == 'não ou coisas muitas fazer para dá legal é python'
inverte("Python é legal? Não sei se da para fazer muitas coisas... Talvez sim.") == 'sim talvez coisas muitas fazer para da se sei não legal é python'
"""
    s1 = str.lower(s)
    s2 = retira_pontuacao(s1)
    ls = str.split(s2)
    list.reverse(ls)
    s3 = str.join(" ", ls)
    return s3