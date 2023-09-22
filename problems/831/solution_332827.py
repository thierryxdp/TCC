def lingua_p(x):
    r = ""
    for Y in x:
        if Y in "aeiouéáú":
            r = r + Y + "p" + Y
        else:
            r = r + Y
	return r