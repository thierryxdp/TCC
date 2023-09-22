def retira_pontuacao(frase):
    """Retorna a frase dado sem caracteres de pontuacao e com espaco no lugar.
    str->str"""
    return str.replace(str.replace(str.replace(str.replace(str.replace(frase,'!',' '),',',' '),'.',' '),'?',' '),'-',' ')

def inverte(frase):
    """Dada uma frase, retorna uma outra frase que contenha as mesmas palavras da frase de entrada na ordem inversa, sem
    letras maiusculas, e sem a pontuacao.
    str->str"""
    p=retira_pontuacao(frase)
    m=p.lower()
    s=m.split()
    f=s[::-1]
    return ' '.join(f)