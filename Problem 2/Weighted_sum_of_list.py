# base method O(n^2)
def bounds_of_rotations(x, c):
    all_combinations = []
    # rotate the list
    for _ in range(len(x)):
        x.append(x.pop(0))
        weighted_sum = 0
        # get sum of the weighted list
        for i, k in enumerate(x):
            weighted_sum += (c ** i) * k
        all_combinations.append(weighted_sum)
        
    return (min(all_combinations), max(all_combinations))


# for bonus question 1 O(2*n) round off to O(n)
def bounds_of_rotations_1(x, c):
    n = len(x)
    # find sum of current list
    value = 0.
    for i in range(1, n+1):
        print(x[-i])
        value *= c
        value += x[-i]
        print(value)
    
    # test all the rotations and save the one with the highest/lowest value
    low = value
    high = value
    for i in range(n):
        value -= x[i]
        value /= c
        value += x[i] * c**(n-1)
        if value < low:
            low = value
        elif value > high:
            high = value

    return (low, high)



# for bonus question 2 also O(2*n) round off to O(n)
def bounds_of_rotations_2(x):
    n = len(x)
    # find sum of current list
    value = 0.
    for i, v in enumerate(x):
        value += i*v
    list_total = sum(x)
    
    # test all the rotations and save the one with the highest/lowest value
    low = value
    high = value
    for i in range(n):
        value -= list_total
        value += n*x[i]
        if value < low:
            low = value
        elif value > high:
            high = value

    return (low, high)

