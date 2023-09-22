def retira_pontuacao(frase):
    if frase[len(frase) - 1] == '?':
        return str.replace(frase, '?' , '')
    
    if frase[len(frase) - 1] == '!':
        return str.replace(frase, '!' , '')

    if frase[len(frase) - 1] == '.':
        return str.replace(frase, '.', '')

    if frase[len(frase) - 1] == '...':
        return str.replace(frase, '...', '')

    if frase[len(frase) - 1] == ':':
        return str.replace(frase,':', '')

    if str.count(frase,',')>0:
        return str.replace(frase,',', '')