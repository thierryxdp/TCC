def retira_pontuacao(frase):
    '''funcao que ao receber uma dada frase, retira todos os caracteres de pontuacao, substituindo por espaço
    string -> string'''
    frase_sem_ponto = str.replace(frase,'-',' ')
    frase_sem_ponto = str.replace(frase_sem_ponto,'.',' ')
    frase_sem_ponto = str.replace(frase_sem_ponto,',',' ')
    frase_sem_ponto = str.replace(frase_sem_ponto,';',' ')
    frase_sem_ponto = str.replace(frase_sem_ponto,':',' ')
    frase_sem_ponto = str.replace(frase_sem_ponto,'!',' ')
    frase_sem_ponto = str.replace(frase_sem_ponto,'?',' ')
    return frase_sem_ponto

def inverte(frase):
    '''funcao que retorna as mesmas palavras da frase de entrada, porem na ordem inversa, sem letras maiusculas e sem pontuacao
    string -> string'''
    frase_minuscula = str.lower(frase)
    frase_minuscula = retira_pontuacao(frase_minuscula)
    frase_minuscula = (str.split(frase_minuscula))[::-1]
    return str.join(' ',frase_minuscula)