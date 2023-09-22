def retira_pontuacao(x):
    """funçao que substitui todas as pontuaçoes por espaço;
    string->string"""
    x = str.replace (x,"-", " ")
    x = str.replace (x, ",", " ")
    x = str.replace (x, ":", " ")
    x = str.replace (x, ";", " ")
    x = str.replace (x, "!", " ")
    x = str.replace (x, ".", " ")
    x = str.replace (x, "?", " ")
    x = str.replace (x, "...", " ")
    return x