def conta_frases():
    string = "Preciso tirar um cochilo. Meu deus! Que horas são? Vou perder minha aula..."
    x = string.count('. ')
    y = string.count('! ')
    z = string.count('...')
    w = string.count('? ')
    total = x+y+z+w
    return total