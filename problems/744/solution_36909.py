def hashtag(s):
    if len(s)%2==0:
        pausa=len(s)//2
	else:
        pausa=(len(s)-1)//2
	return ('#'+s[:pausa]+'#'s[pausa:]+'#')