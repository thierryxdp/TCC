def lingua_p(palavra):
    vogais=['a','e','i','o','u','á','é','í','ó','ú','â','ê','ô','ã','õ']
    papalapavrapa=str.lower(palavra)
    papalapavrapa=list(papalapavrapa)
    for i in len(papalapavrapa):
        if papalapavrapa[i] in vogais:
            papalapavrapa[i]=papalapavrapa[i]+'p'+papalapavrapa[i]
    papalapavrapa=str.join(papalapavrapa)
    return papalapavrapa