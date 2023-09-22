def lingua_p(palavra):
    """Função que recebe uma palavra e retorna a mesma
       traduzida para língua do p."""
    palavra1 = palavra.lower()
    palavra2 = ''
    for p in palavra1:
        vogais = 'aãáeéiíoóuú'
        palavra2 += p
        if p in vogais:
            palavra2 += 'p' + p
    return palavra2