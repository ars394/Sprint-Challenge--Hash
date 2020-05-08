def has_negatives(a):
    d = {}
    result1 = []
    for i in a:
        d[i] = True
    
    for k, v in d.items(): 
        if k > 0 and 0 - k in d:
            result1.append(k)

    return result1


if __name__ == "__main__":
    print(has_negatives([-1,-2,1,2,3,4,-4]))