def media_matriz(media):
    x = 0
    y = 0
    for i in media:
        x = sum(i) + x
        y = len(i) + y
    return (x/y,2)