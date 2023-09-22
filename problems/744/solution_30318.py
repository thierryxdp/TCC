# função coloca o caractere "#" 
# str-> str
def hashtag(s):
    "função coloca o caractere '#' no início, no meio e no final dela"
    media = len(s) //2
    	return "#" + s[0:media] + "#" s[media:] + "#"