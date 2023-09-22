def lingua_p(palavra):
    """
    	Retorna a palavra inserida na língua do P
        str -> str
    """
    palavra_P=palavra.lower()
    repete={}
    for l in range(len(list(palavra))):
        repete[palavra.lower()[l]]=list(palavra).count(palavra[l])
    repete=list(repete)
    for i in range(len(repete)):
        if palavra.lower()[i] in 'aeiouáéíóúàèìòùâêîôûãõ':
            palavra_P = palavra_P.replace(repete[i],repete[i]+'p'+repete[i])
    return palavra_P