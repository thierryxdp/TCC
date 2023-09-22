def conta_frases(Texto):
    #A função recebe uma str

    #A função conta quantos pontos existem
    Contador_de_reticencias = Texto.count('...')
    Contador_de_exclamacao = Texto.count('!')
    Contador_de_interrogacao = Texto.count('?')
    Contador_de_pontos = Texto.count('.')
    
    #Caso exista reticencias a função irá contar duas vezes o numero de pontos, assim, basta subtrair 3 vezes o numero de reticencias dos casos em que existem reticencias
    if(Contador_de_reticencias > 0):
        return Contador_de_reticencias + Contador_de_exclamacao + Contador_de_interrogacao + Contador_de_pontos - 3*Contador_de_reticencias
    else:
        return Contador_de_exclamacao + Contador_de_interrogacao + Contador_de_pontos