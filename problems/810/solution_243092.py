def retira_pontuacao(frase):
    """
    Função que dada uma frase, retorna a frase onde todos os caracteres
    de pontuação tenham sido substituídos por espaço.
    """
    a=str.replace(frase,"..."," ")
    b=str.replace(a,"."," ")
    c=str.replace(b,"!"," ")
    d=str.replace(c,"?"," ")
    e=str.replace(d,"—"," ")
    f=str.replace(e,","," ")
    g=str.replace(f,":"," ")
    h=str.replace(g,";"," ")
    return h

def inverte(frase):
    """
    
    """
    frase2=retira_pontuacao(frase)
    [minuscula]=str.lower(frase2)
    list.sort(minuscula,reverse=True)
    return str.join(" ",minuscula)