class Node:
    def __init__(self,data):
        self.prev=None
        self.data=data
        self.next=None
class DoublyLinkedList:
    def __init__(self):
        self.head=None
    def InsertAtBeg(self,data):
        New_node=Node(data)
        if self.head is None:
            self.head=New_node
        else:
            New_node.next=self.head
            self.head.prev=New_node
            self.head=New_node
    def InsertAtEnd(self,data):
        New_node=Node(data)
        if self.head is None:
            self.head=New_node
        else:
           temp=self.head
           while temp.next:
               temp=temp.next
           temp.next=New_node
           New_node.prev=temp
    def InsetAtPos(self,data,pos):
        New_node=Node(data)
        if self.head is None:
            self.head=New_node
        else:
            temp=self.head
            while pos>=2:
                temp=temp.next
                pos=pos-1
            print(temp.data)
            New_node.prev=temp
            New_node.next=temp.next.next
            temp.next=New_node
            temp.next.prev=New_node
            
    def Delatbeg(self):
        if self.head is None:
            print("Empty")
        else:
            self.head=self.head.next
    def DelatEnd(self):
        if self.head is None:
            print("Empty")
        else:
            temp=self.head
            while temp.next.next:
                temp=temp.next
            temp.next=None
    def Delatkey(self,key):
        temp=self.head
        while temp.next.data !=key:
            temp=temp.next
        temp.next.next.prev=temp
        temp.next=temp.next.next

    def printlist(self):
        temp=self.head
        while temp:
            print(temp.data,end="-->")
            temp=temp.next
        print("None")
D=DoublyLinkedList()
D.InsertAtBeg(1)
D.InsertAtBeg(2)
D.InsertAtBeg(3)
D.InsertAtBeg(4)
D.InsertAtBeg(6)
D.InsertAtBeg(55)
D.InsertAtBeg(33)
D.InsertAtEnd(5)
D.InsetAtPos(22,5)
D.Delatbeg()
D.DelatEnd()
D.printlist()