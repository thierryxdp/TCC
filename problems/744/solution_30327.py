def hashtag(s):
    "função coloca o caractere '#' no início, no meio e no final dela. string-->string"
	media = len(s) //2
    return "#" + s[0:media] + "#" s[media:] + "#"