def flatten(lis):
    result = []
    for i in lis:
        if isinstance(i,list):
            result +=flatten(i)
        else:
            result.append(i)
    return result

d=[1,2,[1,2],[[1]]]
f=flatten(d)
print(f)