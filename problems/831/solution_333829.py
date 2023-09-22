def lingua_p(palavra):
    minusculo = palavra.lower()
    palavra_p = ""
    vogais = "aeiouAEIOUáéíóú"
    for p in minusculo:
        palavra_p += p
        if p in vogais:
            palavra_p += 'p' + p
    
    return palavra_p