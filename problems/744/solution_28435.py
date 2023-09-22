def hashtag(s):
    '''
    Insere # ao longo da string
        Parametros:
            s: str
        Saida: str
    '''
    if len(s)%2==0:
        return "#" + s[0:int(len(s)/2)] + "#" + s[int(len(s)/2):] + "#"
    else:
        return "#" + s[0:int((len(s)/2)-0.5)] + "#" + s[int((len(s)/2)-0.5):] + "#"