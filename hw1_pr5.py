'''There are n people in a line queuing to buy
tickets, where the 0
th person is at the front of the line and the (n − 1)th
person is at the back of the line.
You are given a 0-indexed integer array tickets of length n where the
number of tickets that the ith person would like to buy is tickets[i].
Each person takes exactly 1 second to buy a ticket. A person can only
buy 1 ticket at a time and has to go back to the end of the line (which
happens instantaneously) in order to buy more tickets. If a person does
not have any tickets left to buy, the person will leave the line.
Return the time taken for the person at position k (in 0 indexed array)
to finish buying tickets.
The run-time must be in O(nk).
Example 1.
Input: tickets = [2,3,2], k = 2
Output: 6
Explanation:
• In the first pass, everyone in the line buys a ticket and the line
becomes [1, 2, 1].
• In the second pass, everyone in the line buys a ticket and the line
becomes [0, 1, 0].
The person at position 2 has successfully bought 2 tickets and it took
3 + 3 = 6 seconds.'''
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


