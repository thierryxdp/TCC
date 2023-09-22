def primo(n):

	if n == 2:
		return True

	if n%2 == 0 or n == 1:
		return False

	i = 3
	while i<int(n**0.5)+1:
		if n%i == 0:
			return False
		i += 2

	return True