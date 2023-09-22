def hashtag (x):
    x = "#" + x[:len(x)//2] + "#" + x[len(x)//2:] + "#"
    return x