class Node:
    def _init_(self,data):
        self.data=data
        self.next=None
        self.prev=None
class DLL:
    def _init_(self):
        self.head=None
        self.temp=None
    def creation(self):
        num=int(input("Enter the no of nodes:"))
        for i in range(num):
            data=int(input("Enter the no of datas for the nodes:"))
            newnode=Node(data)
            if self.head is None:
                self.head=newnode
                self.temp=newnode
            else:
                self.temp.next=newnode
                newnode.prev =self.temp 
                self.temp=newnode
    
    def display(self):
        self.temp=self.head
        while self.temp is not None:
            print(self.temp.data, end ="->")
            self.temp=self.temp.next
        print("None")
        
    def insertionAtBegin(self):
        print("Insertion At Begin of the list:")
        data=int(input("Enter the node data:"))
        newnode=Node(data)
        newnode.next=self.head
        self.head.prev=newnode
        self.head=newnode
        
    def insertionAtEnd(self):
        print("Insertion At End of the list:")
        data=int(input("Enter the node value add in end of the list:"))
        newnode=Node(data)
        self.temp=self.head
        while self.temp.next is not None:
            self.temp=self.temp.next
        self.temp.next=newnode
        newnode.prev=self.temp
        
    def insertionAtMiddle(self):
        print("Insertion At Middle of the list:")
        data=int(input("Enter the data value:"))
        newnode=Node(data)
        position=int(input("Enter the position value:"))
        self.temp=self.head
        for i in range(position-1):            
            #prev=self.temp
            self.temp = self.temp.next
        newnode.next=self.temp
        newnode.prev=self.temp.prev
        self.temp.prev.next=newnode
        self.temp.prev=newnode
        
    def DeletionAtBegin(self):           
        print("Deletion At Begin of the list:")
        self.temp=self.head
        self.head=self.temp.next
        self.head.prev= None
        del(self.temp)    
        
    def DeletionAtEnd(self):
        print("Deletion At End of the list:")
        self.temp=self.head
        while self.temp.next is not None:
             prev=self.temp
             self.temp=self.temp.next
        prev.next=None
        del(self.temp)    
    def DeletionAtMiddle(self):
        print("Deletion At Middle of the list:")
        position=int(input("Enter the position value to remove:"))
        self.temp=self.head
        for i in range(position-1):
            prev=self.temp
            self.temp=self.temp.next
        prev.next=self.temp.next
    def count(self):
        print("count the Nodes:")
        c=1
        self.temp=self.head
        while self.temp.next is not None:
            self.temp=self.temp.next
            c=c+1
        print(c)
    
    def searchingelement(self):
        value=int(input("Enter  the data to search the node:"))
        self.temp=self.head
        while self.temp.next is not None:
            if (self.temp.data==value):
                print("The element is  found  in the Node")
            else:
                self.temp=self.temp.next
        if(self.temp.data==value):
            print("The element is found in the node.")
        else:
            print("The element is found in the node.")    
    
        
a=DLL() 
a.creation()
a.display()   
a.insertionAtBegin()
a.display()   
a.insertionAtEnd()
a.display()
a.insertionAtMiddle()
a.display()
a.DeletionAtBegin()
a.display()
a.DeletionAtEnd()
a.display()
a.DeletionAtMiddle()
a.display()
a.count()
a.searchingelement()