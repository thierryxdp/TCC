def inverte(frase):
    """Recebe uma frase e inverte a ordem de suas palavras"""
    nova_frase = retira_pontuacao(frase)
    nova_frase = nova_frase.split(' ')
    nova_frase = nova_frase[::-1]
    return str(nova_frase)