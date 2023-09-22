def uppCons(frase):
    """essa funçao recebe uma frase como entrada e a retorna com as consoantes em maiuscula e o resto igual como estava na frase original"""
    """entrada: str"""
    """saida: str"""
    texto=''
    indice=0
    while indice<len(frase):
        if frase[indice] not in 'AÁÃEÉIÍOÕÓUaãáeéíioõóuú':
            texto=texto+str.upper(frase[indice])
        else:
            texto=texto+frase[indice]
        indice=indice+1
    return texto