def conta_frases(txt):
    """função que conta o número de frases em um texto txt, em que as frases são divididas por '.','!','?' e '...'"""
    quantfrase=txt.split(".")
    quantfrase2=quantfrase.split("!")
    quantfrase3=quantfrase2.split("?")
    quantfrase4=quantfrase3.split("...")
    return len(tuple[quantfrase4])