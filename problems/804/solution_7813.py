def filtra_pares(tupl):
    sol=()
    if tupl[0]%2==0:
        sol+=(tupl[0],)
        if tupl[1]%2==0:
            sol+=(tupl[1],)
        	if tupl[2]%2==0:
                sol+=(tupl[2],)
        		if tupl[3]%2==0:
                	sol+=(tupl[3],)
                    return sol
                return sol
            return sol
        return sol
    elif tupl[0]%2==0:
        sol+=(tupl[0],)
        if tupl[2]%2==0:
            sol+=(tupl[2],)
        	if tupl[3]%2==0:
                sol+=(tupl[3],)
                return sol
            return sol
        return sol
    elif tupl[0]%2==0:
        sol+=(tupl[0],)
        if tupl[3]%2==0:
            sol+=(tupl[3],)
            return sol
        return sol
    elif tupl[1]%2==0:
        sol+=(tupl[1],)
        if tupl[2]%2==0:
            sol+=(tupl[2],)
            if tupl[3]%2==0:
                sol+=(tupl[3],)
                return sol
            return sol
        return sol