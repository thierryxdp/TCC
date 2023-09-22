def lingua_p(x):
    """A fução adiciona a letra P apos cada vogal
    str --> str """
    r = ""
    for Y in x:
        if Y in "aeiouéáú":
            r = r + Y + "p" + Y
        else:
            r = r + Y
	return r