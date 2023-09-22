def retira_pontuacao(frase):
    '''retira e retorna a pontuação da frase
    str->str'''
    frasenova=''
    for i in range(len(frase)):
        if frase[i] == ',' or frase[i] == '-' or frase[i] == ':' or frase[i] == ';' or frase[i] == '!' or frase[i] == '?' or frase[i] == '.':
            frasenova = frase[:i]  + frase[i+1:]

	return frasenova

def inverte(frase):
    frasesemmaiuscula = frase.casefold()
    frase = retira_pontuacao(frasesemmaiuscula)
    fraseseparada = str.split(frase,' ')
    novafrase=[]
    for i in range(len(fraseseparada)):
        novafrase.append(fraseseparada[len(fraseseparada)-1-i])
    frasefinal=str.join(' ',novafrase)
    return frasefinal