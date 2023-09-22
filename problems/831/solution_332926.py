def procura_acentuacao(x, s):
    '''
    Busca o caractere x na string s 
    Devolve: índice da primeira ocorrência de x em s 
    e -1 se x não for encontrado em s
    ''' 
    for j in range(len(s)):
        if x == s[j]: return j
    return -1

def limpa_acentuacao(s):
    '''
    Função recebe uma string contendo texto com acentuações da língua portuguesa
    Retorna uma string contendo texto sem acentuações
    '''
    acentM = "áàâãéêíóõôúÁÀÂÃÉÊÍÓÕÔÚçÇ"
    acentV = "aaaaeeiooouAAAAEEIOOOUcC"
    t = ""
    for ch in range(len(s)):
        # verifica se é acentuada ou não
        k = procura_acentuacao(s[ch], acentM)
        if k >= 0: # acentuada
            t = t + acentV[k] # converte
	    else: # não acentuada
            t = t + s[ch]
    return t


def lingua_p(frase):
    '''
    Funçao que dada uma frase, troque todas as vogais das palavras
    consideradas por pela mesma vogal e o p.
    '''
   
    frase=limpa_acentuacao(frase)
    frase_nova = frase[:]
    for vogal in ["a", "e", "o", "u"]:
        frase_nova = str.replace(frase_nova, vogal,'p'+vogal)
    return frase_nova