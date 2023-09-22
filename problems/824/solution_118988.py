def uppCons (s):
    for e in s if e not in ["AEIOUaeiou"]:
        str.upper (e)
	return s