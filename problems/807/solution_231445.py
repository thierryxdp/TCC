def conta_frases(frase):
    n_ret = len(frase.split('...')) - 1
    n_final = len(frase.split('.')) - 1
    n_exc = len(frase.split('!')) - 1
    n_int = len(frase.split('?')) - 1
    
    n_frases = n_final - (n_ret*3) + n_ret + n_exc + n_int
    return n_frases