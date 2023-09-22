def lingua_p(palavra):
    """A função definida recebe uma palavra (em português).
    Todas as vogais da palavra original devem ser sucedidas
    pela letra'p' mais a vogal original que antecede 'p'. 
    Ao retornar essa palavra - traduzida toda em minúsculo,
    devem ser feitas todas essas modificações.
    Entrada: String
    Saída: String"""
    
    str.lower(palavra)
    palavra_nova=palavra[i]
    vogais='aàáãâeéêiíoóôõuûú'
    i=0
    novap=0
    
    for palavra[i] in vogais:
        if palavra_nova[i] in 'aàáãâ':
            novap = ''.join(listap)
        elif palavra_nova[i] in 'eéê':
            novap = ''.join(listap)
        elif palavra_nova[i] in 'ií':
            novap = ''.join(listap)
        elif palavra_nova[i] in 'oóôõ':
            novap = ''.join(listap)
        elif palavra_nova[i] in 'uûú':
            novap = ''.join(listap)
    i +=1
    ''.join(listap)
    return novap