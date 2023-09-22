def lingua_p (palavra):
    '''insere a letra p apos cada vogal da palavra original
    e tambem insere a propria vogal apos o p
    str -> str'''

    palavra2 = str.lower(palavra)

    lista = list(palavra2)

    i = 0
    
    tamanho = len(lista)
    
    while i < tamanho:
        if lista[i] in 'aeiouáéíóúàèìòùãõâêîôû':
                
            lista[i+1:i+1] = 'p'
            lista[i+2:i+2] = lista[i]

            tamanho = len(lista)
            
            i += 2
        i += 1

    letras_juntas = ''.join(lista)
            
    return letras_juntas