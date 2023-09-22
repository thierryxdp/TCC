def retira_pontuacao (frase):
    teste = frase.split("...")
    a = teste.count ('.')
    b = frase.count ('!')
    c = frase.count ('?')
    d = frase.count ('...')
    return a + b + c + d + teste