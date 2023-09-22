def procura_acentuacao(x, s):
    '''
    Busca o caractere x na string s 
    devolve: índice da primeira ocorrência de x em s -1 se x não for encontrado em s
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

def retira_pontuacao(texto):
    ''' 
    Função recebe um texto e remove caracteres especiais que estão em uma lista pre-definida
    '''
    # usando replace () para remover caracteres especiais
    caracteres_interesse = "@_!'^#$%^&*()<>?/\|}{:;[]~,...-"
    texto = limpa_acentuacao(texto)
    for i in caracteres_interesse:
        texto = texto.replace(i, ' ')
        texto = texto.lower()
    return texto

def inverte(frase):
    '''
    Funçao que dada uma frase retorne uma outra frase contendo
    as mesmas palavras da frase de entrada na ordem inversa.
    '''
    frase = retira_pontuacao(frase)
    lista = str.split(frase)
    lista.reverse()
    frase = str.join(" ", lista)
    return frase