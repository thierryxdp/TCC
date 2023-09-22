def conta_frases(txt):
    """função que conta a quantidade de frases em um texto txt, frases essas que são divididas pelos caracteres '.','!','?' e '...'; str-->int"""
    
    texto=txt.replace('.'or'!'or'?'or'...','/')
    texto=txt.split('/')
    
    return len(texto)