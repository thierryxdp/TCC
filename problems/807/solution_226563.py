def conta_frases(txt):
    """função que conta a quantidade de frases em um texto txt, frases essas que são divididas pelos caracteres '.','!','?' e '...'; str-->int"""
    
    texto=txt.replace('...','/')
    texto2=texto.replace('!','/')
    texto3=texto2.replace('?','/')
    texto4=texto3.replace('.','/')
    textofin=texto4.split('/')
    
    return len(textofin)-1