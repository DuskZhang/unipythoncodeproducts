class DLinkedListNode:
    # An instance of this class represents a node in Doubly-Linked List
    def __init__(self,initData,initNext,initPrevious):
        self.data = initData
        self.next = initNext
        self.previous = initPrevious
        
        if initNext != None:
            self.next.previous = self
        if initPrevious != None:
            self.previous.next = self
            
    def getData(self):
        return self.data
    
    def setData(self,newData):
        self.data = newData
        
    def getNext(self):
        return self.next
    
    def getPrevious(self):
        return self.previous
    
    def setNext(self,newNext):
        self.next = newNext
        
    def setPrevious(self,newPrevious):
        self.previous = newPrevious


class DLinkedList:
    # An instance of this class represents the Doubly-Linked List
    def __init__(self):
        self.__head=None
        self.__tail=None
        self.__size=0        
           
    def search(self, item):
        current = self.__head
        found = False
        while current != None and not found:
            if current.getData() == item:
                found= True
            else:
                current = current.getNext()
        return found
        
    def index(self, item):
        current = self.__head
        found = False
        index = 0
        while current != None and not found:
            if current.getData() == item:
                found= True
            else:
                current = current.getNext()
                index = index + 1
        if not found:
                index = -1
        return index        
         
    def add(self, item):
        # adds an item at the start of the list
        if self.__head != None: #nonempty
            new_node = DLinkedListNode(item,self.__head,None)
            self.__head = new_node
        else: #empty
            new_node = DLinkedListNode(item,None, None)
            self.__tail = new_node
            self.__head = new_node    
        self.__size = self.__size + 1
        
    def remove(self,item):
        # remove the node containing the item from the list
        if self.__size == 0:
            raise Exception('List is Empty')
        current = self.__head
        previous = None
        found = False
        while current != None and not found:
            if current.getData() == item:
                found = True
            else:
                previous = current
                current = current.getNext()
        if found:
            if self.__size == 1:
                self.__head = None
                self.__tail = None
            elif previous == None: # the item is in the first node of the list
                self.__head = current.getNext()
                self.__head.setPrevious(None)
            elif current.getNext() == None: 
                self.__tail = current.getPrevious()
                self.__tail.setNext(None) 
            else: # item is in middle
                previous.setNext(current.getNext())
                current.getNext().setPrevious(previous)
            self.__size -=1
        
    def append(self,item):
        # adds an item at the end of the list
        if self.__tail != None:
            new_node = DLinkedListNode(item,None, self.__tail) #prev is self.__tail
            self.__tail = new_node
            
        else: #empty list
            new_node = DLinkedListNode(item,None, None) 
            self.__tail = new_node    
            self.__head = new_node
        self.__size = self.__size +1
        
    def insert(self, pos, item):
        # – adds a new node (containing the item as its data) at the given position 
        assert isinstance(pos,int), ("Position not an integer")
        assert pos >= 0, ("Integer out of range")
        if self.__size == 0 or pos >= self.__size:
            self.append(item)
        elif pos == 0:
            self.add(item)
        else:
            i = 1
            previous = self.__head
            while previous.getNext() != None and i != pos:
                previous = previous.getNext()
                i+=1
            DLinkedListNode(item,previous.getNext(),previous)
            self.__size += 1
    def pop1(self):
        assert self.__size > 0, ("Error: Empty list")
        val = self.__tail.getData()
        if self.__size == 1:
            self.__tail = None
            self.__head = None
        else:
            self.__tail = self.__tail.getPrevious()
            self.__tail.setNext(None)
        self.__size -= 1
        return val
    
    def pop(self, pos=None):
        if pos == None:
            return self.pop1()
        else:
            assert isinstance(pos,int), ("Pos not an integer")
            assert pos >= 0 and pos < self.__size, ("Pos not in range")
            current = self.__head
            i = 0
            while current != None and i!= pos:
                current = current.getNext()
                i+=1
            val = current.getData()
            if self.__size == 1:
                self.__tail = None
                self.__head = None
            elif i == 0:
                self.__head = self.__head.getNext()
            elif i == self.__size - 1:
                self.__tail = self.__tail.getPrevious() 
            current.setNext(None)
            current.setPrevious(None)
            self.__size -= 1
            return val
                

    def searchLarger(self, item):
        current = self.__head
        i = 0
        while current != None:
            if current.getData() > item:
                return i
            current = current.getNext()
            i += 1
        return -1
        
    def getSize(self):
        return self.__size
    
    def getItem(self, pos):
        assert pos >= -self.getSize() and pos <= self.getSize() - 1, ("Pos not in range")
        if pos < 0:
            current = self.__tail
            i = -1
            while current != None and i != pos:
                current = current.getPrevious()
                i -= 1    
            return current.getData()
        else:
            current = self.__head
            i = 0
            while current != None and i != pos:
                current = current.getNext()
                i += 1    
            return current.getData()
        
    def __str__(self):
        current = self.__head
        string = ''
        while current.getNext() != None:
            string = string + str(current.getData())+' '
            current = current.getNext()
        string+=str(current.getData())
        return string


def test():
                  
    linked_list = DLinkedList()
                    
    is_pass = (linked_list.getSize() == 0)
    assert is_pass == True, "fail the test"
            
    linked_list.add("World")
    linked_list.add("Hello")    
    is_pass = (str(linked_list) == "Hello World")
    assert is_pass == True, "fail the test"
              
    is_pass = (linked_list.getSize() == 2)
    assert is_pass == True, "fail the test"
            
    is_pass = (linked_list.getItem(0) == "Hello")
    assert is_pass == True, "fail the test"
        
        
    is_pass = (linked_list.getItem(1) == "World")
    assert is_pass == True, "fail the test"    
            
    is_pass = (linked_list.getItem(0) == "Hello" and linked_list.getSize() == 2)
    assert is_pass == True, "fail the test"
            
    is_pass = (linked_list.pop(1) == "World")
    assert is_pass == True, "fail the test"     
            
    is_pass = (linked_list.pop() == "Hello")
    assert is_pass == True, "fail the test"     
            
    is_pass = (linked_list.getSize() == 0)
    assert is_pass == True, "fail the test" 
                    
    int_list2 = DLinkedList()
                    
    for i in range(0, 10):
        int_list2.add(i)      
    int_list2.remove(1)
    int_list2.remove(3)
    int_list2.remove(2)
    int_list2.remove(0)
    is_pass = (str(int_list2) == "9 8 7 6 5 4")
    assert is_pass == True, "fail the test"
    
    for i in range(11, 13):
        int_list2.append(i)
    is_pass = (str(int_list2) == "9 8 7 6 5 4 11 12")
    assert is_pass == True, "fail the test"
                
    for i in range(21, 23):
        int_list2.insert(0,i)
    is_pass = (str(int_list2) == "22 21 9 8 7 6 5 4 11 12")
    assert is_pass == True, "fail the test"
                
    is_pass = (int_list2.getSize() == 10)
    assert is_pass == True, "fail the test"    
                    
    int_list = DLinkedList()
                    
    is_pass = (int_list.getSize() == 0)
    assert is_pass == True, "fail the test"                   
                    
    for i in range(0, 1000):
        int_list.append(i)      
    correctOrder = True
            
    is_pass = (int_list.getSize() == 1000)
    assert is_pass == True, "fail the test"            
            
        
    for i in range(0, 200):
        if int_list.pop() != 999 - i:
            correctOrder = False
                            
    is_pass = correctOrder
    assert is_pass == True, "fail the test" 
            
    is_pass = (int_list.searchLarger(200) == 201)
    assert is_pass == True, "fail the test" 
            
    int_list.insert(7,801)   
        
    is_pass = (int_list.searchLarger(800) == 7)
    assert is_pass == True, "fail the test"
            
            
    is_pass = (int_list.getItem(-1) == 799)
    assert is_pass == True, "fail the test"
            
    is_pass = (int_list.getItem(-4) == 796)
    assert is_pass == True, "fail the test"
                    
    if is_pass == True:
        print ("=========== Congratulations! Your have finished exercise 2! ============")

                
if __name__ == '__main__':
    test()