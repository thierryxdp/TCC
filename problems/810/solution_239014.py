def inverte(Frase, frase):
    '''Função que dada uma frase como entrada retorne uma 
    outra com as mesmas palavras mas em ordem inversa e sem
    pontuação e letras maiúsculas.
    string --> string'''
    frase = frase.replace(";"," ")
    frase = frase.replace("-"," ")
    frase = frase.replace("!"," ")
    frase = frase.replace("?"," ")
    frase = frase.replace(","," ")
    frase = frase.replace(":"," ")
    frase = frase.replace("."," ")
    return frase
    Frase = Frase.lower()
    Frase= Frase.split()
    Frase= separador.join[::-1]
    return Frase + retira_pontuacao(frase)