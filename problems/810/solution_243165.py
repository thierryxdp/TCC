def inverte(frase):
    """Função que retira a pontuação de uma frase e inverte a ordem das palavras da mesma frase. 
    Na entrada a função recebe uma frase (string) e na saída ela devolve
    essa mesma frase(string) sendo substituido a pontuação por espaço e a ordem das palavras alteradas"""
    texto1 = frase.replace('!',' ')
    texto2 = texto1.replace('.',' ')
    texto3 = texto2.replace(',',' ')
    texto4 = texto3.replace('-',' ')
    texto5 = texto4.replace(':',' ')
    texto6 = texto5.replace(';',' ')
    texto7 = texto6.replace('?',' ')
    junto = texto7.split()
    espaco = ' '.join(junto[::-1])
    return espaco.lower()