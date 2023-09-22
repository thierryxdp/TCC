def lingua_p(palavra):
    """Dado uma palavra qualquer, retorna essa palavra escrita na 
    lingua do p:
    str-->str"""
    palavra.lower()
    palavra_final=''
    for letra in palavra:
        if letra in 'aeiou':
            palavra_final+=letra+'p'
        palavra_final+=letra
    return palavra_final