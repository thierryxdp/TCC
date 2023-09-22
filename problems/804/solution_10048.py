def hashtag(x):
    if (len(x)%2)==0:
        return '#' +x[0:(len(x)/2)] + '#' + x[(len(x)/2)+1:len(x)] +'#'