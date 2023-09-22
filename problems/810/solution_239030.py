def inverte(Frase):
    '''Função que dada uma frase como entrada retorne uma 
    outra com as mesmas palavras mas em ordem inversa e sem
    pontuação e letras maiúsculas.
    string --> string'''
    Frase = retira_pontuacao(Frase)
    Frase = frase.lower()
    Frase = frase.split()
    nova_frase =" ".join(Frase[::-1])
    return Frase