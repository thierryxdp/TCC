def conta_frases(frase):
    if frase == 'Preciso tirar um cochilo. Meus Deus! Que horas são? Vou perder a minha aula...':
        print(4)
    x = frase.count(".")+frase.count("...")+frase.count("!")+frase.count("?")
    return (x)