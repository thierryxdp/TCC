def retira_pontuacao(frase):
    """funcao que dado de entrada uma frase, retorna a 
    propria frase onde todos os caracteres de pontuacao
    sao substituidos por espaço;
    str -> str"""
    return str.replace(str.replace(str.replace(str.replace(str.replace(str.replace(str.replace(str.replace(frase,'-',' '),',',' '),':',' '),';',' '),'!',' '),'?',' '),'...',' '),'.',' ')

def minuscula(frase1):
    """ funcao que dado de entrada uma frase, retorna a mesma
    com todas as letras minusculas;
    str -> str"""
    return str.lower(frase1)

def inverte(frase2):
    """funcao que dado de entrada uma frase, retorna uma
    outra frase contendo as mesmas palavras da frase de 
    entrada na ordem inversa, sem letras maiusculas, e sem
    a pontuacao;
    str -> str"""
    return list.reverse(str.split(minuscula(retira_pontuacao(frase2))))