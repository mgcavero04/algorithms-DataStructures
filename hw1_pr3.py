import random
''''#1.Extend the LinkedList class adding the following new methods:'''
'''a)The method called first_index_of(x) that returns the
index of the first from the left node with value x. If there is no such
node, return None.
The index here is how many nodes away from the head our node is.
E.g., applying first_index_of(5) to the linked list [1 → 7 → 5 →
4 → 2], we get 2; applying it to [1 → 2 → 3 → 4 → 5 → 6 → 5],
we get 4.
The run-time must be in O(n).
b)The method called get_middle() that returns a list of
values of the middle node(s) of a linked list. If the list has an odd
number of nodes, there will be only one middle node; otherwise,
there will be two middle nodes.
E.g., applying get_middle() to the linked list [1 → 7 → 5 → 4 → 2],
we get [5]; applying it to [1 → 2 → 3 → 4 → 5 → 6], we get [3, 4].
The run-time must be in O(n).'''

class Node:
    def __init__(self, value=None, next=None):
        self.value = value
        self.next = next
        self.prev = None
    def __str__(self):
        return f'Node [{self.value}]'
    def getData(self):
        return self.value
    
class LinkedList:
    def __init__(self):
        self.first = None
        self.last = None
       
    def insert(self, x):
        if self.first == None:
            self.first = Node(x, None)
            self.last = self.first
        elif self.last == self.first:
            self.last = Node(x, None)
            self.first.next = self.last
        else:
            current = Node(x, None)
            self.last.next = current
            self.last = current   

    def clear(self):
        self.__init__()
    def first_index_of1(self, x): #1).1.Returns the index of the first from the left node with value x. If there is no suchnode, return None.
        current=self.first
        index=0
        
        #res = [self(i) for i in self]
        
        while current != None:
           print(current)
           if x == current.getData():
                     
                return index
           index += 1
           current=current.next
            
        return 'None'
    
    def get_length(self):
        current=self.first
        count=0
        while current != None:
            count=count+1
            current=current.next
        print("length is:")
        return count
    def getEven(self):
        
        
        return ''
    def get_middle(self):#1).2.The method called get_middle() that returns a list of values of the middle node(s) of a linked list. If the list has an odd number of nodes, there will be only one middle node; otherwise, there will be two middle nodes
        current=self.first
        length = self.get_length()
        mid_index = length // 2
        remainder = length%2
        
        while mid_index:
            prev=current
            current=current.next
            mid_index -= 1
        if remainder==0:
            return prev.getData(), current.getData()
        else:    
            return current.getData()
        #return self.getEven()
def main(): 
    val=4
    test=LinkedList()
    test.insert('a')
    test.insert('b')   
    test.insert(val)
    test.insert('c')
    test.insert('d')
    test.insert('e')
    #print(test.first_index_of1(val))
    #print(test.get_length())
    print(test.get_middle())

if __name__ == "__main__":
    main()

