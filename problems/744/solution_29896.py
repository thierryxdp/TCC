def hashtag(s):
    """ retorne uma str com "#" no ínicio, no meio e no fim, str -> str"""
    return ('#')+(s[0:len(s)//2])+('#')+(s[len(s)//2:])+('#')