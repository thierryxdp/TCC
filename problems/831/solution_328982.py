def lingua_p(palavra):
    '''Funcao que, dada a ocorrencia de uma vogal em uma palavra,
    retorna a palavra com a adicao da letra P + a vogal depois da
    ocorrencia em questao. Exemplo: alice -> apalipicepe.
    Str -> Str'''
    palavra_em_p: ''
    for letra in palavra:
        if letra in 'aeiouãáâéíóõúAEIOUÃÁÂÉÍÓÕÚ':
            palavra_em_p += palavra[str.index(palavra,letra): str.index(palavra, letra)+1] + 'p' + letra
        else:
            palavra_em_p += palavra[str.index(palavra,letra): str.index(palavra, letra)+1]
    return palavra_em_p