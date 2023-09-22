def conta_frases(s):
    """calcula e retorna o número de frases contidas num texto 's';str->int"""
    return int(len(str.split(str(s),'!')))+int(len(str.split