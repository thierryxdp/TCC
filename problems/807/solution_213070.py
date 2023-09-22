def conta_frases(texto):
	num = str.split(texto,".")
    num = str.split(num,"!")
    num = str.split(num,"?")
    num = str.plit(num,"...")
	return len(num)