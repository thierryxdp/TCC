def conta_frases(texto):
    """dado um texto, a função retorna o número de frases desse texto;
    str->int"""
    A=str.split(texto,'...')
    B=str.split(str(A),'!')
    C=str.split(str(B),'?')
    D=str.split(str(C),':')
    E=str.split(str(D),'.')
    frases= str.split(str(E),',')
    return (len(frases)-1)