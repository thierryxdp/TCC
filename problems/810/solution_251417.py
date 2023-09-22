def retira_pontuacao(frase):
    '''Retira todos os caracteres de pontuação de uma frase, os substituindo por um espaço
    entrada: str
    saída: str
    '''
    return str.replace(str.replace(str.replace(str.replace(str.replace(str.replace(str.replace(str.replace(frase, '...',' '),'-',' '), '.', ' '),':', ' '),';', ' '), '?', ' '), '!', ' '),',', ' ')
def inverte(frase):
    '''Inverte a ordem das palavras de uma frase;
    entrada: str;
    saída: str;
    '''
    listafrase= str.split(retira_pontuacao(frase))
    list.reverse(listafrase)
    frasereversa = str.replace(str.replace(str.replace(str.replace(str.replace(str.replace(str.replace(str.replace(str(listafrase), "',", ''), '",', ''), ' "', ' '), " '", ' '), "['", ''), '["', ''), '"]', ''), "']", '')
    frasefinal = str.lower(frasereversa)
    return frasefinal