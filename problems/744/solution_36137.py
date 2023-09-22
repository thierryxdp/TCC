def hashtag(s):
    meio=(len(s))/2
    return '#'+(s[0: int(meio)]) +'#'+(s[int(meio): len(s)])+'#'