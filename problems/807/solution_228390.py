def conta_frases(texto):
    '''função que dado um texto, retorna o número de frase desse texto;str->int'''
    frasepontof=list(str.partition(texto,'.'))
    frasepontoi=list(str.partition(texto,'?'))
    frasepontoe=list(str.partition(texto,'!'))
    frasepontor=list(str.rstrip(texto,'...'))
    frasepontof=frasepontof[0]+frasepontof[1]
    frasepontoi=frasepontoi[0]+frasepontoi[1]
    frasepontoe=frasepontoe[0]+frasepontoe[1]
    resposta=[frasepontof]+[frasepontoi]+[frasepontoe]+[frasepontor]
    return len(resposta)