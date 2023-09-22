def retira_pontuacao(frase):
    """Dada de entrada uma frase, retorna a mesma frase só que com pontuação substituida por espaço
    str=>str"""
    return str.replace(str.replace(str.replace(str.replace(str.replace(frase,'!',' '),'-',' '),'.',' '),',',' '),':',' ')