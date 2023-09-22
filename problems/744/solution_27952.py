# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# str-> str
def hashtag(s):
    """concatena hastags no início, meio e fim das strings;string->string"""
    if len(s)==10:
        return '#'+ s[:5]+ '#' + s[5:]+'#'
    else:
        if len(s)==9 or len(s)==8:
            return '#'+s[:4]+'#'+s[4:]+'#'
        else:
            if len(s)==7 or len(s)==6:
                return '#'+s[:3]+'#'+s[3:]+'#'
            else:
                if len(s)==5 or len (s)==4:
                    return '#'+s[:2]+'#'+s[2:]+'#'
                else:
                    if len(s)==3 or len (s)==2:
                        return '#'+s[:1]+'#'+s[1:]+'#'
                    else:
                        if len(s)==1:
                            return '#'+s+'#''#'
                        else:
                            if len(s)==11 or len(s)==12:
                                return '#'+s[:6] +'#'+s[6:]+'#'
                            else:
                                if len(s)==13 or len(s)==14:
                                    return '#'+s[:7]+'#'+s[7:]+'#'