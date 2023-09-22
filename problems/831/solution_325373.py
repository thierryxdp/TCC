def lingua_p(palavra):
    '''
    Tranforma uma palavra, em português, traduzindo-a para a língua do P, que,
    após cada vogal da palavra original, insere a sequência: letra 'p' mais a
    vogal original.
    str -> str

    Parameters:
    palavra: Parâmetro textual, do tipo string (str).

    Returns:
    A palavra original traduzida para a língua do P.

    O teste do código foi realizado utilizando valores elucidativos do tipo
    textual, de modo que o resultado gerado pelo código seja condizente com
    o resultado previsto na solução manual do problema.
    '''
    
    vogais = ['a', 'e', 'i', 'o', 'u','á','é','í','ó','ú','ã','õ','à','è',
              'ì','ò','ù']
    
    palavra = str.lower(palavra)
    palavra = list(palavra)

    palavra_linguaP = []
    
    for letra in palavra:
        if letra in vogais:
            palavra_linguaP += letra + ('p') + letra
        else:
            palavra_linguaP += letra

    palavra_traduzida = ''.join(palavra_linguaP)
    return palavra_traduzida