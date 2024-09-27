from collections import deque
class Tickets:
    
    def time(substract, k):#
        
        time=0
        kIndex=0
        
        while kIndex < len(substract)*substract[k]:
            l=len(substract)
            counter=0 
            for i in substract: 
               print("time:", time)
               print("kIndex:", kIndex)
               print("counter:",counter)
               print("i:",i)
               if kIndex <= k:
                  time += min(substract[k], i)
               else:
                  time += min(substract[k] - 1, i)
               
               kIndex +=1
            return time   
        
        
               
    
    
def main(): 
        
        print(Tickets.time([1,2,5,2,1], 2))

if __name__ == "__main__":
        main()


