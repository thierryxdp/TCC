def inverte(texto):
    """Põe frase de traz para a frente ; str ==>str"""
    nova_frase = retira_pontuacao(texto)
    nov= nova_frase.split()
    print (nov)
    ac= nov[::-1]
    act=  ' '.join(ac)
    return act