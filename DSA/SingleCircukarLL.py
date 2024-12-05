class Node:
    def __init__(self,data) -> None:
        self.data=data
        self.next=None
class SingleCircularLL:
    def __init__(self) -> None:
        self.head=None
    def InsertAtbeg(self,data):
        new_node=Node(data)
        if self.head is None:
            self.head=new_node
            new_node.next=self.head

        else:
            temp=self.head
            while temp.next!=self.head:
                temp=temp.next
            temp.next=new_node
            new_node.next=self.head
            self.head=new_node
    def InsertAtEnd(self,data):
        new_node=Node(data)
        if self.head is None:
            self.head=new_node
            new_node.next=self.head
        else:
            temp=self.head
            while temp.next!=self.head:
                temp=temp.next
            temp.next=new_node
            new_node.next=self.head
    def delatbeg(self):
        if self.head is None:
            print("empty")
        else:
            temp=self.head
            while temp.next!=self.head:
                temp=temp.next
            self.head=self.head.next
            temp.next=self.head
    def delatend(self):
        if self.head is None:
            print("empty")
        else:
            temp=self.head
            while temp.next.next!=self.head:
                temp=temp.next
            temp.next=self.head
    def delatkey(self,key):
        if self.head is None:
            print("empty")
        else:
            temp=self.head
            while temp.next.data!=key:
                temp=temp.next
            temp.next=temp.next.next
    def printlist(self):
        temp=self.head
        while True:
            print(temp.data,end="-->")
            temp=temp.next
            if temp==self.head:
                break
    
sc=SingleCircularLL()
sc.InsertAtbeg(5)
sc.InsertAtbeg(6)
sc.InsertAtbeg(7)
sc.InsertAtEnd(11)
sc.InsertAtEnd(12)
sc.delatbeg()
sc.delatend()
sc.delatkey(5)
sc.printlist()

