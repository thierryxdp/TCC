def conta_frases(txt):
    """Função que dado um texto txt, conta quantas frases existem, sendo essas delimitadas por '.','!','?' e '...';str-->str"""
    txt.count('.')
    txt.count('!')
    txt.count('?')
    txt.count('...')
    return txt.count('.')+txt.count('!')+txt.count('?')+txt.count('...')