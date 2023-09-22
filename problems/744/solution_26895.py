def hashtag(s):
    '''retorna uma hashtag no início, no meio e no fim da string recebida
    str-> str'''
    meio=len(s)/2
    MeioImpar=math.floor(len(s)/2)
    if len(s)%2==0 and 0<len(s)<2:
        return '#'+s[:meio]+'#'+s[meio:]+'#'
    elif 0<len(s)<2:
        return '#'+s+'#'
    if s=='':
        return ''
    else: 
        return '#'+s[:MeioImpar]+'#'+s[MeioImpar:]+'#'