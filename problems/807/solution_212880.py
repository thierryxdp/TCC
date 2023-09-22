def conta_frases(x):
    """funçao que calcula quantas frases aparecem no texto de acordo com a pontuaçao;
    string->int"""
    x = str.replace(x,"...","!")
    return str.count(x,".") + str.count(x,"!") + str.count(x,"?") + str.count(x,"...")