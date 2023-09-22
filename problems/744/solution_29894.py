def hashtag(s):
    """ retorne uma str com "#" no ínicio, no meio e no fim, str -> str"""
    return ('#')+(s[0:str(len)(s)//2])+('#')+(s[str(len(s)//2):])+('#')