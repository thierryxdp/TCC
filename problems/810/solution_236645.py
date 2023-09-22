def retira_pontuacao(frase):
    """Dada de entrada uma frase, retorna a mesma frase só que com pontuação substituida por espaço
    str=>str"""
    return str.replace(str.replace(str.replace(str.replace(str.replace(str.replace(frase,'!',' '),'-',' '),'.',' '),',',' '),':',' '),'?',' ')

def inverte(frase1):
    """Dado uma frase1 retorna uma frase sem letras maiúsculas, sem pontuação e invertida
    str=>str"""
    frase_nova = str.split(retira_pontuacao(str.lower(frase1)),"")
    frase_nova1 = str.join(" ",frase_nova[::-1])
    return frase_nova1[1:]