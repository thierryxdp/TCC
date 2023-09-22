def media3 (a,b,c):
    '''calcula a media de 3 numeros inteiros'''
    return (a+b+c)/3

def min_media3 (a,b,c):
    '''calcula a soma do menor numero com a media'''
    return min(a,b,c) + media3 (a,b,c)