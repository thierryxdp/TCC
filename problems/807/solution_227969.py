def conta_frases(srtr):
    srtr.replace('...', '.')
    return str.count(srtr.replace('...', '.'), '.')