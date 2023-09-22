def conta_frases(txt):
    """Função que dado um texto txt, conta quantas frases existem, sendo essas delimitadas por '.','!','?' e '...';str-->str"""
    return txt.count('.|!|?|...')