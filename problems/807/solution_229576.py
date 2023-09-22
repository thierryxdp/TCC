def conta_frases(s):
    """Função que quando informado frases que terminam com pontuações como ("...",".","!","?"), retorna o número de frases informadas
str -> int
testes:
conta_frases("Preciso tirar um cochilo. Meus Deus! Que horas s̃ao? Vou perder a minha aula...") == 4
conta_frases("Victor Marinho. Estuda computação... É professor? Um dia vai se formar...") == 4
"""
    str.count(s,"...")
    s2 = str.replace(s,"...", '#######')
    str.count(s2,".")
    str.count(s2,"!")
    str.count(s2,"?")
    return (str.count(s,"...") + str.count(s2,"!") + str.count(s2,".") + str.count(s2,"?"))