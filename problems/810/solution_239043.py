def inverte(frase):
    '''Função que dada uma frase como entrada retorne uma 
    outra com as mesmas palavras mas em ordem inversa e sem
    pontuação e letras maiúsculas.
    string --> string'''
    frase = frase.replace(";"," ")
    frase = frase.replace("-"," ")
    frase
    frase = frase.replace("!"," ")
    frase = frase.replace("?"," ")
    frase
    frase = frase.replace(","," ")
    frase = frase.replace(":"," ")
    frase
    frase = frase.replace("."," ")
    return frase
    frase = retira_pontuacao(Frase)
    frase = frase.lower()
    frase = frase.split()
    nova_frase =" ".join(Frase[::-1])
    return nova_frase + retira_pontuacao(frase)