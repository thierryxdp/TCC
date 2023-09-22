def retira_pontuacao(frase):
    """A função retorna uma frase onde todos os caracteres de pontuação
    tenham sidos substituídos por espaços.
    str-->str"""
    if "," in frase:
        frase = str.replace(frase,","," ")
    if ":" in frase:
        frase = str.replace(frase,":"," ")
    if "." in frase:
        frase = str.replace(frase,"."," ")
    if ";" in frase:
        frase = str.replace(frase,";"," ")
    if "?" in frase:
        frase = str.replace(frase,"?"," ")
    if "!" in frase:
        frase = str.replace(frase,"!"," ")
    
    lista_frase = frase.split(" ")
    posicao = len(lista_frase) + 1
    inverte = lista_frase[posicao:-(posicao): -1]
    concatenar = str.join(" ",inverte)
    
    return str.lower(concatenar)