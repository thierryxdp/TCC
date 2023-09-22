def retira_pontuacao(frase):
    '''retira e retorna a pontuação da frase
    str->str'''
    
    for i in range(len(frase)):
        if frase[i] == ',' or frase[i] == '-' or frase[i] == ':' or frase[i] == ';' or frase[i] == '!' or frase[i] == '?' or frase[i] == '.':
            frase = frase[:i]  + ' ' + frase[i+1:]

	return frase

def inverte(frase):
    frasesemmaiuscula = frase.lower()
    frase = retira_pontuacao(frasesemmaiuscula)
    frase= frase.strip()
    fraseseparada = str.split(frase,' ')
    novafrase=[]
    a=0
    for i in range(len(fraseseparada)):
        if fraseseparada[len(fraseseparada)-1-i] == '' and fraseseparada[len(fraseseparada)-2-i] == '':
      	a=0
        else:
            novafrase.append(fraseseparada[len(fraseseparada)-1-i])
    frasefinal=str.join(' ',novafrase)
    return frasefinal