def inverte(frase):
    '''A funcao recebe uma frase e retorna uma outra frase que conetnha as mesmas palavras
    da frase de entrada na ordem inversa, sem letras maiusculas e sem a pontuacao.
    Parametro de entrada: str
    Valor de retorno: str'''
    #Retirando as letras maiusculas
    frase=str.lower(frase)
    #Retirando a pontuacao:
    if "—" in frase:
        frase=str.replace(frase,"—"," ")
    if "-" in frase:
        frase=str.replace(frase,"-"," ")
    if "," in frase:
        frase=str.replace(frase,","," ")
    if ":" in frase:
        frase=str.replace(frase,":"," ")
    if ";" in frase:
        frase=str.replace(frase,";"," ")
    if "." in frase:
        frase=str.replace(frase,"."," ")
    if "!" in frase:
        frase=str.replace(frase,"!"," ")
    if "?" in frase:
        frase=str.replace(frase,"?"," ")
    if "..." in frase:
        frase=str.replace(frase,"..."," ")
    #Separando as palavras, gerando uma lista, e invertendo a lista
    frase=str.rstrip(frase)
    frase=str.lstrip(frase)
    lista=str.split(frase," ")
    lista=lista[::-1]
    #Juntando as palavras da lista em uma string
    outrafrase=str.join(" ",lista)
    return outrafrase