class Node:
    def __init__(self,data):
        self.prev=None
        self.data=data
        self.next=None
class DobulycircularLL:
    def __init__(self):
        self.head=None
    def InsertAtBeg(self,data):
        new_node=Node(data)
        if self.head is None:
            self.head=new_node
            new_node.prev=self.head
            new_node.next=self.head
        else:
            temp=self.head
            while temp.next!=self.head:
                temp=temp.next
            new_node.prev=temp
            new_node.next=self.head
            self.head.prev=new_node
            temp.next=new_node
            new_node=self.head
    def InsertAtEnd(self,data):
        new_node=Node(data)
        if self.head is None:
            self.head=new_node
            new_node.prev=self.head
            new_node.next=self.head
        else:
            temp=self.head
            while temp.next!=self.head:
                temp=temp.next
            new_node.prev=temp
            new_node.next=self.head
            temp.next=new_node
            self.head.prev=new_node
    def InsertAtKey(self,data,pos):
        new_node=Node(data)
        if self.head is None:
            self.head=new_node
            new_node.prev=self.head
            new_node.next=self.head
        else:
            temp=self.head
            while pos>2:
                temp=temp.next
                pos=pos-1
            new_node.prev=temp
            new_node.next=temp.next
            temp.next.prev=new_node
            temp.next=new_node
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
            while temp.next!=self.head:
                temp=temp.next
            temp.prev.next=self.head
            self.head=temp.next
    def delatkey(self,key):
        if self.head is None:
            print("empty")
        else:
            temp=self.head
            while temp.next.data!=key:
                temp=temp.next
            temp.next.next.prev=temp
            temp.next=temp.next.next
    def printlist(self):
         temp=self.head
         while True:
            print(temp.data,end="-->")
            temp=temp.next
            if temp==self.head:
                break


dc=DobulycircularLL()
dc.InsertAtBeg(5)
dc.InsertAtBeg(8)
dc.InsertAtBeg(9)
dc.InsertAtBeg(10)
dc.InsertAtBeg(11)
dc.InsertAtBeg(12)
dc.InsertAtEnd(6)
dc.InsertAtKey(44,2)
dc.delatbeg()
dc.delatend()
dc.delatkey(10)
dc.printlist()