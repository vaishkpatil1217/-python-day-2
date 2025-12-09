def min_max(no):
    if not no:
        return (None, None) 
    
    min1 = min(no)
    max2= max(no)
    return (min1, max2)


no = [10, 5, 20, 2, 15]
total = min_max(no)
print(f"Original numbers:",no)
print(f"Minimum and maximum values:",total)