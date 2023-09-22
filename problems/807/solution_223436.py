def conta_frases(txt):
    interrogacao= str.count(txt,'?')
    exclamacao= str.count(txt,'!')
    reticencias= str.cont(txt,'...')
    final=str.count(txt,'.')
    return final+interrogacao+exclamacao+reticencias+final