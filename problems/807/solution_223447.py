def conta_frases(txt):
    interrogacao= str.count(txt,'?')
    exclamacao= str.count(txt,'!')
    reticencias= str.count(txt,'...')
    final= str.count(txt,'.')
    return interrogacao+exclamacao+final+int(reticencias)/5