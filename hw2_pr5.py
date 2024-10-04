from decimal import Decimal
from operator import itemgetter
''''' Greedy: You are given a list of n tuples (a[i], b[i]), each tuple represents a segment [ai, bi], i = 1, 2, . . . , n, on a line.
Return the maximum integer k such that some point on the line is covered with k segments.The run-time must be in O(n log n).    '''
def range_intersection1(list):

    startNumbers=[i[0] for i in list]
    endNumbers=[i[-1] for i in list]
    print("startNumbers:", startNumbers)
    minIntersection_end = min(endNumbers)
    maxIntersection_start = max(x for x in startNumbers if x <= minIntersection_end)#Here is the max intersection
    print("maxIntersection_start:", maxIntersection_start)
    new_list = [tup for tup in list if maxIntersection_start not in tup]
    new_list = [tup for tup in list if minIntersection_end not in tup]
    #if maxIntersection_start <= minIntersection_end :
    intersectionPoints=(maxIntersection_start, minIntersection_end)
    intersectionsPoint=intersectionPoints[0]
    
    for interval in new_list:
        if interval[0] <= intersectionsPoint <= interval[1]:
           intersectionPoints=intersectionPoints + (interval,)
           print("intersectionPoints:", intersectionPoints)
    count = len(intersectionPoints)
    return count  
    # ------------------------------------------------------------------
def range_intersection2(list):
     minIntersection_end = min(list, key = itemgetter(1))[1]
     #maxIntersection_start =max(list)
     sorted_list_by_secondElement = sorted(list, key=lambda x: x[1])
     print("minIntersection_end:",minIntersection_end)
     selected_list = [tup for tup in list if minIntersection_end in tup]#tuples with min end value en tuples
     new_list=sorted_list_by_secondElement[0]
     print("new_list", new_list)
     counter=1
     for m in range(1, len(sorted_list_by_secondElement)):
        if sorted_list_by_secondElement[m] >= sorted_list_by_secondElement[counter]:
            new_list+ sorted_list_by_secondElement[m]
            counter=m
     return m



if __name__ == "__main__":
    range1 = (-0.3, 2.7)
    range2 = (-1, 0.5)
    range3= (2.5, 3.3)
    range4= (-0.7, 2.3)
    range5=(0.5, 1.7)
    list=[range1, range2,range3, range4, range5]
    result = range_intersection2(list)

    if result:
        print(f"Intersection: {result}")
    else:
        print("No intersection found.")
    
   
