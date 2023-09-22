def conta_frases(texto):
    texto1= texto.split('.')
    texto2=texto1.split('...')
    texto3=texto2.split('!')
    texto4=texto3.split('?')
    resp= len (texto4)
    return resp