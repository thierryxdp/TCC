def total(list,supermarket):
    '''it returns the total cost of a shopping of the avalables list' products in supermarket
    list,dictionary -> float'''
    cost=0
    for product in list:
        if product in supermarket:
            cost+= supermarket[product]
    return round(cost,2)