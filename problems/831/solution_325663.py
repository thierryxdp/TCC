def lingua_p(palavra):
    """Função que recebe uma palavra em português,
    retornando essa mesma palavra na língua do P
    entrada: str
    retorno: str"""
    palavra_nova=''
    palavra=palavra.lower()
    i=0
    while i < len(palavra):
        if palavra[i] in 'aeiouáéíóú':
            palavra_nova= palavra_nova+palavra[i]+'p'+palavra[i]
        else:
            palavra_nova= palavra_nova+ palavra[i]
        i= i + 1
    return palavra_nova