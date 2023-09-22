def lingua_p(palavra:str)->str:
    '''retorna a frase dada no parâmetro traduzida para a língua do p.
    uma palavra foi traduzida para a língua do P quando,
    após cada vogal da palavra original,  ́e inserida a 
    sequência de letras p mais a vogal original.'''
    lingua = ''
    for letra in palavra:
        if letra in 'AEIOUaeiouÁÉÍÓÚáéíóúÂÊÎÔÛâêîôûãõ':
            letra = str.lower((letra)+'p'+(letra))
        lingua = lingua + letra
    return lingua