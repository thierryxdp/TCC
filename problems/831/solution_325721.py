def lingua_p(palavra):
    """Dada uma palavra em português a função retorna esta mesma palavra
    traduzida para língua do P, isto é, será inserido após cada vogal da
    palavra original a letra 'p' mais a vogal original;
    str -> str"""
    texto = ''
    palavra1 = str.lower(palavra)
    for x in palavra1:
        if x in 'aeiou':
            txt = str.upper(x+'p'+x)
            palavra1 = str.replace(palavra1,x,txt)
    return str.lower(palavra1)