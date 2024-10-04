def arrayIntersection(array1,array2):
    ''''Problem 6. Given two integer arrays, return an array of their intersection. Each i in the result must appear as many times as it shows in both arrays and you may return the result in anyorder.'''
    intersection=[]
    for i in array2:
        
            if i in array1:
                array1.remove(i)
                intersection.append(i)
                             
    return intersection
    


def arrayIntersectionImproved(array1, array2):
    counts = {}
    arrayIntersection=[]
    intersection=[]
    for i in array2:
        if i in array1:
            array1.remove(i)
            intersection.append(i)

    for item in intersection:# conventional way to create a frequency dictionary from a list
        if item in counts:
            counts[item] += 1
        else:
            counts[item] = 1
    for key, value in counts.items():
        arrayIntersection.extend([key] * value)
    return arrayIntersection 


if __name__ == "__main__":
    array1=[3,7,2,6,6,9,5,1,1]
    array2=[9,4,9,8,6,1,0,6,6]
    print(arrayIntersectionImproved(array1,array2))
    
