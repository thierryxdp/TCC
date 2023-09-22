def retira_pontos(frase):
    """Recebe uma frase e retorna ela sem nenhum tipo de pontuação, sendo substituida por espaços;
    	str -> str"""
    frase=str.replace(frase,'.',' ')
    frase=str.replace(frase,',',' ')
    frase=str.replace(frase,'-',' ')
    frase=str.replace(frase,'...',' ')
    frase=str.replace(frase,'!',' ')
    frase=str.replace(frase,'?',' ')
    return frase
def inverte(frase):
    """Recebe uma frase e devolve ela invertida, sem nenhuma pontuação;
    	str -> str"""
    retira_pontos(frase)
    frase=str.lower(frase)
    frase=str.split(frase)
    frase=list.reverse(frase)
    frase=str.join('',frase)
    return frase