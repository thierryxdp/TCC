def primo(n):
    final=0
    for i in range(n):
        if n%(i+1)==0:
            final=final+1
    if final ==2:
        return True
	else:
        return False