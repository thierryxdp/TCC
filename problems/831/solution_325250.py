def lingua_p(palavra):
    """Função que dada uma palavra, a retorna na língua do p (após cada vogal da
palavra original é inserida a sequência de letras p mais a vogal original)
    str -> str"""
    palavranova = ''
    for i in range(len(palavra)):
        if str.lower(palavra[i]) not in 'bcdfghjklmnpqrstvwxyzç':
            palavranova += palavra[i] + 'p' + palavra[i]
        else:
            palavranova += palavra[i]
    return str.lower(palavranova)