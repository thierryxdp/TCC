def hashtag(x):
    a='#'
    t=int((len(x)/2))
    b=x[0:t]
    c=x[t:len(x)]
    return a + b + a +  c + a