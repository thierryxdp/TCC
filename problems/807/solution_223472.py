def conta_frases(txt):
    interrogacao= str.count(txt,'?')
    exclamacao= str.count(txt,'!')
    reticencias= str.count(txt,'...')
    final= str.count(txt,'.')
    if '...' in txt:
        return interrogacao+exclamacao+reticencias+(int(final/4))
    else:
        return interrogacao +exclamacao+ final