def conta_frases(texto):
    """Retorna o número de frases que aparecem em um texto dado como entrada.
Obs.: cada texto deve ser terminado por ".", "...", "!" ou "?" e os dois últimos
não podem ser repetidos em sequência.
str -> int"""
    r = str.count(texto,"...")
    p = str.count(texto,".") - r*3
    e = str.count(texto,"!")
    i = str.count(texto,"?")
    return r + p + e + i

#Casos de teste
# conta_frases("Olá! Como você está?") == 2
# conta_frases("Não estou muito bem... estou doente. Mas, e você?") == 3
# conta_frases("Ah, que pena... eu estou bem... agora, irei torcer por sua melhora, ok? Conte comigo!") == 4