class Node:
    def __init__(self, data=None, next=None):
        self.data=data
        self.next=next

head=Node()

lst = [1,2,3,4,5]

def lst_to_ll(lst):
    temp=head
    for data in lst:
        new_node=Node(data,temp.next)
        if(temp.next is None):
            temp.next = new_node
            temp=temp.next

def printll():
    temp=head.next
    while(temp):
        if(temp.next != None):
            print(temp.data, "->", end=" ")
        else: print(temp.data)
        temp = temp.next

lst_to_ll(lst)
printll()