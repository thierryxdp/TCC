def primos(x):
	if (x == 2):
		return 'True'
	elif (x>2 and x%3 == 1):
		return 'true'
	elif (x>2 and x%5 == 1):
		return 'true'
	elif (x>2 and x%7 == 1):
		return 'true'
	elif (x>2 and x%11 == 1):
		return 'true'
	elif (x>2 and x%13 == 1):
		return 'true'
	elif (x>2 and x%17 == 1):
		return 'true'
	elif (x>2 and x%19 == 1):
		return 'true'
	elif (x>2 and x%23 == 1):
		return 'true'
	elif (x>2 and x%29 == 1):
		return 'true'
	elif (x>2 and x%31 == 1):
		return 'true'
	else: return 'false'