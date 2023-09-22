def hashtag(s):
	if len(s) == 1:
		return '##' + s + '#'
	if len(s)%2 == 0:
		t = int(len(s)/2)
		return '#' + s[:t] +'#' + s[t:] + '#'
	else:
		t = int(len(s)/2)
		return '#' + s[:t] +'#'+ s[t:]+'#'