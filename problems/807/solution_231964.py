def conta_frases(x):
    p=['. ','! ', '...','? ','; ',': ']
    for y in p:
        s=str.split(x,y)
        return len(s)