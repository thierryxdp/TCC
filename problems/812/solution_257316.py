def retira_pontuaçao(frase):
    """  funçao que troca elementos de pontuaçao por espaço em branco
    str -> str"""
    texto=str.replace(frase,',',' ')
    texto=str.replace(texto,'-',' ')
    texto=str.replace(texto,'.',' ')
    texto=str.replace(texto,'!',' ')
    texto=str.replace(texto,'?',' ')
    texto=str.replace(texto,';',' ')
    texto=str.replace(texto,':',' ')
    return texto