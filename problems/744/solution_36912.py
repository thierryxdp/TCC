def hashtag(x):
    x=str(x)
    meio=len(x)//2
    return '#'+ x[0:meio]+'#'+x[meio:]+'#'