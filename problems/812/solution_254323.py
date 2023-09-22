def retira_pontuacao(frase):
    if frase[len(frase) - 1] == '!':
        return frase.replace('!' , '')

    if frase[len(frase) - 1] == '.':
        return str.replace(frase, '.', '')

    if frase[len(frase) - 1] == '...':
        return str.replace(frase, '...', '')

    if frase[len(frase) - 1] == ':':
        return str.replace(frase,':', '')
    
    if frase[len(frase) - 1] == '?':
        return frase.replace(', Brute?', 'Brute')
    
    if str.count(frase,',')>0:
        return str.replace(frase,',', '')