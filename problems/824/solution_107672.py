def uppCons(frase):
    """Função que dada uma frase, a retorna com todas as consoantes em maiusculo e as vogais da mesma maneira; str -> str"""
    maiuscula = frase.upper()
    frasefinal = ()
    i = 0
    while i < len(maiuscula):
        if maiuscula[i] in 'AEIOU':
            maiuscula.lower('AEIOU')
            frasefinal = frasefimal + 1
            i = i + 1
            return frasefinal