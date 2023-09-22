def conta_frases(frase):
    frase = str.replace(frase, "...", "***")

    count = 0
    count += str.count(frase, ".")

    count += str.count(frase, "?")
    count += str.count(frase, "***")



    return count



ex1 = "Se Deus criou as pessoas... para* amar e as coisas para cuidar. Por que! amamos as coisas e usamos as pessoas?"
ex2 = "Preciso tirar um cochilo. Meu Deus! Que horas são? Vou perder a minha aula..."
ex3 = "Alguns vão te odiar, fingem que te amam agora. Então... pelas costas, eles tentam te eliminar! Mas quem Jah abençoa, ninguém amaldiçoa."

conta_frases(ex1)
conta_frases(ex2)
conta_frases(ex3)