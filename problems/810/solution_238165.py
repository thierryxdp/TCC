def inverte(texto):
    """função que retorna uma lista com as palavras de uma frase invertidas, sendo dada a frase
 srt ---> str"""
    sem_pontuacao = str.lower(str.replace(str.replace(str.replace(str.replace(str.replace(str.replace(str.replace(texto,"."," "),"!"," "),"?"," "),","," "),"-"," "),":"," "),";"," "))
    separadas = str.split(sem_pontuacao)[::-1]
    return str.join(" ",separadas)