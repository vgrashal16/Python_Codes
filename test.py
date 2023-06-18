class Node:
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next


# def insert_datalist(data_list):
#     temp=head
#     for data in data_list:
#         new_node=Node(data,temp.next)
#         if(temp.next is None):
#             temp.next = new_node
#             temp=temp.next

def print_list():
    temp = head.next
    while(temp):
        print(temp.val)
        temp = temp.next

# def reverseList(head):
#     p=Node()
#     q=Node()
#     temp=head
#     while (temp is not None):
#         q=p
#         p=temp
#         temp=temp.next
#         p.next=q
#     return 
# print(reverseList(head))

def merge(list1,list2):
        head=Node()
        while (head.next is not None):
            if (list1==list2):
                newNode=Node(list1)
                newNode2=Node(list2)
                newNode.next=newNode2
                list1=list1.next
                list2=list2.next
                head=newNode2

            elif (list1>list2):
                newNode=Node(list2)
                head.next=newNode
                list2=list2.next
                head=newNode
    
            elif (list1<list2):
                newNode=Node(list1)
                head.next=newNode
                list1=list1.next
                head=newNode
        return head
head=Node()
list1=[1]
list2=[2]
print(merge(list1,list2))
# data_list = eval(input())
# insert_datalist(data_list)
print_list()