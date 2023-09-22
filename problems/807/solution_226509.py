def conta_frases(txt):
    """função que conta o número de frases em um texto txt, em que as frases são divididas por '.','!','?' e '...'"""
    quantfrase=txt.split("." or "!" or "?" or "...")
    return len(quantfrase)