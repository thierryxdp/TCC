def lingua_p(p):
    h=""
    for e in p:
        if e in "aeiouAEIOUáéíóú":
            h = h + e + "p" + e
        else:
            h = h + e
	return h