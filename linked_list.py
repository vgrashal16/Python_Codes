class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next


# data_1 = Node(5)
# data_2 = Node(6)
# data_3 = Node(7)

# data_1.next = data_2
# data_2.next = data_3

head = Node()

# head.next = data_1**


def print_list():
    temp = head.next
    while(temp):
        if(temp.next != None):
            print(temp.data, "->", end=" ")
        else: print(temp.data)
        temp = temp.next



def insert_at_start(data):
    first_data = head.next
    head.next = Node(data, first_data)


def insert_at_end(data):
    temp = head
    if temp is None:
        temp = Node(data, None)
    while(temp.next):
        temp = temp.next
    temp.next = Node(data, None)


def insert_at_mid(data):
    index = int(input("What index: "))  # 3  2
    temp = head
    while index:
        temp = temp.next
        index = index-1
    next_node = temp.next
    temp.next = Node(data, next_node)
    return

def get_length():
    count=0
    temp=head
    while temp.next:
        temp = temp.next
        count+=1
    return count

def insert_datalist(data_list):
    temp=head
    for data in data_list:
        new_node=Node(data,temp.next)
        if(temp.next is None):
            temp.next = new_node
            temp=temp.next

    def remove_at(index):
        if (index >= 0) and (index < get_length()):
            temp = head
            while index:
                temp = temp.next
                index=index-1
            temp.next=temp.next.next
    else:
        raise Exception("Invalid Index")
    return

data_list=[5,2,6,7,3,4]
insert_datalist(data_list)
# getNewHead = insert_datalist(data_list)
# print_list(getNewHead)
# insert_at_start(4)
# insert_at_start(3)
# insert_at_end(8)
# insert_at_end(9)
remove_at(0)
print(get_length())
print_list()

# print_list()
# insert_at_mid(5)
