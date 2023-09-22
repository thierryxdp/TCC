def retira_pontuacao(frase):
    """A função retorna uma frase onde todos os caracteres de pontuação
    tenham sidos substituídos por espaços.
    str-->str"""
    if "-" in frase:
        frase = str.replace(frase,"-"," ")
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
    return frase




def inverte(frase):
    """A função retorna uma outra frase que contenha as mesmas palavras
    da frase de entrada na ordem inversa, sem maiúscula, e sem a
    pontuação.
    str-->str."""
    
    lista_frase = frase.split(" ")
    posicao = len(lista_frase) + 1
    inverter = nova_lista[posicao:-(posicao): -1]
    concatenar = str.join(" ",inverter)
    
    return str.lower(concatenar)