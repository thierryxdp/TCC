def lingua_p(palavra):
    vogais=['a','e','i','o','u','á','é','í','ó','ú','â','ê','ô','ã','õ']
    papalapavrapa=str.lower(palavra)
    papalapavrapa=list(papalapavrapa)
    vazio_existencial=''
    for i in list(range(len(papalapavrapa))):
        if papalapavrapa[i] in vogais:
            papalapavrapa[i]=papalapavrapa[i]+'p'+papalapavrapa[i]
        vazio_existencial=vazio_existencial+papalapavrapa[i]
    return vazio_existencial