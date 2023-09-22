def lingua_p(palavra):
    """Função que recebe uma palavra e retona ela na lingua no p que a cada vogal encontra retona a palavra com letra P + vogal.
    Parametros: str->str"""
    nova_palavra = ''
    for i in range(len(palavra)):
        if palavra[i] in 'aáàãeéêíioôõóu':
            nova_palavra += palavra[i]+ 'p'+ palavra[i]
        else:
            nova_palavra += palavra[i]
    return nova_palavra