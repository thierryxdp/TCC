def retira_pontuacao(frase):
    """Funcao que dada uma frase, retorna a
frase onde todos os caracteres de pontuacao
(incluindo travessao, virgula, dois pontos, ponto e virgula, alem da pontuacao de
encerramento de frase) tanham sido substituidos por espaco; string -> string"""

    frase = str.replace(frase,"—"," ")
    frase = str.replace(frase,"-"," ")
    frase = str.replace(frase,"."," ")
    frase = str.replace(frase,","," ")
    frase = str.replace(frase,":"," ")
    frase = str.replace(frase,";"," ")
    frase = str.replace(frase,"?"," ")
    frase = str.replace(frase,"!"," ")    
    frase = str.replace(frase,"..."," ")
    return frase

def inverte(frase):
    """Funcao que dada uma frase, retorna uma outra frase que contenha as
mesmas palavras da frase de entrada na ordem inversa, sem letras maiusculas,
e sem a pontuacao; string -> string"""
    
    frase_sem_pontuacao_str = retira_pontuacao(frase)
    frase_semp_sep_list = str.split(frase_sem_pontuacao_str)
    frase_semp_sep_list_inv = frase_semp_sep_list[::-1]
    frase_semp_espaco_str = str.join(" ",frase_semp_sep_list_inv) 
    frasefinal = str.lower(frase_semp_espaco_str)
    
    return frasefinal