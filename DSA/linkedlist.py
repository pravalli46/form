class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class LinkedList:
    def __init__(self):
        self.head=None
    def InsertAtBeg(self,data):
        new_node=Node(data)
        if self.head is None:
            self.head=new_node
        else:
            new_node.next=self.head
            self.head=new_node
    def InsertAtEnd(self,data):
        new_node=Node(data)
        if self.head is None:
            self.head=new_node
        else:
          temp=self.head
          while temp.next:
              temp=temp.next
          temp.next=new_node
    def InsertAtpos(self,data,pos):
        new_node=Node(data)
        if self.head is None:
            self.head=new_node
        else:
            temp=self.head
            while(pos>2):
                temp=temp.next
                pos=pos-1
            new_node.next=temp.next
            temp.next=new_node
    def delbeg(self):
        if self.head is None:
            print("empty")
        else:
            self.head=self.head.next
    def delend(self):
        if self.head is None:
            print("empty")
        else:
            temp=self.head
            while temp.next.next:
                temp=temp.next
            temp.next=None
    def delkey(self,key):
        if self.head is None:
            print("empty")
        else:
            temp=self.head
            while temp.next != None and temp.next.data != key:
                temp=temp.next
            if temp.next is None:
                print("key not found")
            else:
                temp.next=temp.next.next
    def sum(self):
        if self.head is None:
            print("empty")
        else:
            sum=0
            temp=self.head
            while temp:
                sum=temp.data+sum
                temp=temp.next
        return sum
    def linearsearch(self,data):
        temp=self.head
        pos=1
        while temp:
            if temp.data==data:
                print("key found",pos)
            pos=pos+1
            temp=temp.next
    def reverse(self):
        stack=[]
        temp=self.head
        while temp:
            stack.append(temp.data)
            temp=temp.next
        temp=self.head
        while temp:
            temp.data=stack.pop()
            temp=temp.next


    def PrintList(self):
        temp = self.head
        while temp:
            print(temp.data,end="-->")
            temp=temp.next
        print("None")
        
L=LinkedList()
L.InsertAtBeg(5)
L.InsertAtBeg(6)
L.InsertAtBeg(7)
for i in range(1,10):
    L.InsertAtEnd(i)
L.delbeg()
L.delend()
L.PrintList()
L.reverse()
L.PrintList()
L.linearsearch(7)
print(L.sum())


