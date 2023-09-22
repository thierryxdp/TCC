def lingua_p(frase):
    """Esta é a função que dada uma frase retorna ela traduzida para a lingua do P, colocando após cada vogal, essa vogal e a letra P; str -> str"""
    frase_minuscula = frase.lower()
    
    for letra in "aeiouáéíóú":
        
        letra_p = letra + 'p' + letra
        frase_minuscula = frase_minuscula.replace(letra,letra_p)

    return frase_minuscula