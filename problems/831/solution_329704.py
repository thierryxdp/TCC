def lingua_p(palavra):
    """ Função que traduz a palavra para a língua do P
    str -> str """
    x='AEIOUaeiouáéíóú'
    lista=[]
    palavra_final=''
    for letra in palavra:
        if letra in x:
            lista=lista+[letra+'p'+letra]
        else:
            lista=lista+[letra]
    for parte in lista:
        palavra_final=palavra_final+parte
    return palavra_final