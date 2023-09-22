def filtra_pares(a,b,c,d):
    if a%2==0 and b%2==0 and c%2==0 and d%2==0:
        x=a,b,c,d
	else:
        if a%2==0 and b%2==0 and c%2==0:
        	x=a,b,c
		else:
            if a%2==0 and b%2==0 and d%2==0:
        		x=a,b,d
            else:
                if a%2==0 and c%2==0 and d%2==0:
        			x=a,c,d
                else:
                    if b%2==0 and c%2==0 and d%2==0:
        				x=b,c,d
                    else:
                        if a%2==0 and b%2==0:
        					x=a,b
                        else:
                            if a%2==0 and c%2==0:
        						x=a,c
                            else:
                                if a%2==0 and d%2==0:
        							x=a,d
                                else:
                                    if b%2==0 and c%2==0:
        								x=b,c
                                    else:
                                        if b%2==0 and d%2==0:
        									x=b,d
                                        else:
                                            if c%2==0 and d%2==0:
        										x=c,d
                                            else:
                                                if a%2==0:
        											x=a
                                                else:
                                                    if b%2==0:
        												x=b
                                                    else:
                                                        if c%2==0:
        													x=c
                                                        else:
                                                            if d%2==0:
        														x=d
	return x