def lingua_p(palavra):
    palavra = palavra.lower()
    lingua_p = ''
    for i in range(len(palavra)):
        lingua_p+=palavra[i]
        if palavra[i] in 'aeiouéáú':
            lingua_p+='p'+palavra[i]
    return lingua_p