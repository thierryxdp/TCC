def lingua_p(palavra):
    p = str.lower(palavra)
    r = ""
    for i in range(0, len(p)):
        if p[i] not in "aeiou":
            r = r + p[i]
		if p[i] in "aeiou":
            r = r + p[i] + "p" + p[i] 
	return r