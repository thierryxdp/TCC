def conta_frases(s):
    """Função que quando se é informada frases que terminam com pontuações como ("...",".","!","?"), retorna o número de frases ditas.
    assinatura: str -> int
    testes:
    conta_frases("Eu estou muito cansada. Eu imploro férias, UFRJ! Por favor!")
    conta_frases("Mientras mi mente viaja donde tú estás. Mi padre grita otra vez. Yo soy rebelde! Cuando no sigo a los demás.") """
    str.count(s, "...")
    s2 = str.replace(s,"...", '#######')
    str.count(s2,".")
    str.count(s2,"!")
    str.count(s2,"?")
    return (str.count(s,"...") + str.count(s2,"!") + str.count(s2,".") + str.count(s2,"?"))