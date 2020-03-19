Remove the documentation string i.e ''' ''' to make the code work for each function below. I have implemented all the functions such as
1.appendnode
2.length
3.display
4.reverse
5.insert
6.delete_by_pos
7.printRev
8.middle
9.merge
10.mergeSort
11.linaerSearch

Go to line 206 for implementation of functions. Hope this helps :)

class Node:
    def __init__(self, data):
        "constructor to initiate this object"

        # store data
        self.data = data

        # store reference (next item)
        self.next = None
        return

    def has_value(self, value):
        "method to compare the value with the node data"
        if self.data == value:
            return True
        else:
            return False


def appendnode(head,item):
    "add an item at the end of the list"
    #print("In appendnode function")
    if not isinstance(item, Node):
        item = Node(item)

    if head is None:
        head = item
    else:
        th=head
        while th.next:
            th=th.next
        th.next = item
        #th=th.next

    tail = item

    return

def length(head):
    "returns the number of list items"
    #print("In length function")
    count = 0
    current_node = head

    while current_node is not None:
        # increase counter by one
        count = count + 1

        # jump to the linked node
        current_node = current_node.next

    return count

def display(head):
    "outputs the list (the value of the node, actually)"
    #print("In display function")
    current_node = head

    while current_node.next is not None:
        print(current_node.data,end=' -> ')

        # jump to the linked node
        current_node = current_node.next
    print(current_node.data)
    return

def reverse(h):

    " Reverse the linked list (Recursive code)"
    #print("In reverse function")
    if h==None or h.next==None:
        return h
    r=reverse(h.next)
    h.next.next=h
    h.next=None
    return r

def insert(head,val,pos):

    " Insert a value 'val' at a position 'pos' of a linked list whose head is 'head' "
    #print("In insert function")
    th=head
    if pos < 0 or pos-1 >= length(head):
        print(pos,'is an invalid index')
        return th
    if pos==0:
        print('inserting at 0')
        val=Node(val)
        val.next=th
        head=val
        return val
    pos-=1
    curr_pos=0
    curr_node=head
    while pos!=0:
        curr_pos+=1
        curr_node=curr_node.next
        pos-=1
    val=Node(val)
    val.next=curr_node.next
    curr_node.next=val
    return th

def delete_by_pos( head,pos):

    " Delete a value given its position of a linked list "
    #print("In delete_by_pos function")
    th=head
    th2=th
    if pos<0 or pos>=length(head):
        print(pos,'is an invalid index')
        return th
    if pos==0:
        print('pos is 0')
        head=head.next
        return head
    print('Deleting index',pos)
    pos-=1
    while pos!=0:
        th=th.next
        pos=pos-1
    th.next=th.next.next
    return th2

def printRev(head):

    #It just prints in reverse order, it does not manipulate original list
    #print("In printRev function")
    if head==None:
        return
    printRev(head.next)
    print(head.data,end=' -> ')

def middle(h,flag):

    "Find middle element. If length(Linked list) is even then , if flag is true return (n/2 - 1)th element , else is flag is false return (n/2)th element "
    #print("In middle function")
    s,f=h,h
    while f!=None and f.next!=None and f.next.next!=None:
        s=s.next
        f=f.next.next
    if flag==True:
        return s
    return s.next

def merge(h1, h2):

    " Merge two sorted linked lists of heads h1 and h2"
    #print("In merge function")
    d = Node('a')
    td=d
    while h1 != None and h2 != None:
        if h1.data < h2.data:
            d.next = h1
            h1 = h1.next
        else:
            d.next = h2
            h2 = h2.next
        d = d.next
    if h1 != None:
        d.next = h1
    if h2 != None:
        d.next = h2
    return td.next

def mergeSort(h):

    " Sort a linked list using merge sort"
    #print("In mergesort function")
    if h==None or h.next==None:
        return h
    m=middle(h,True)
    sh=m.next
    m.next=None
    return merge(mergeSort(h),mergeSort(sh))

def linearSearch(head, value):
    "search the linked list for the node that has this value"
    #print("In linearSearch function")
    if head==None:
        return False
    th=head
    while th:
        if th.data==value:
            return True
        th=th.next
    return False



#Working successfully

'''
#Insert function
h1=Node(1)
insert(h1,17,1)
insert(h1,18,2)
insert(h1,19,3)
insert(h1,8,2)
insert(h1,20,4)
insert(h1,10,10)
display(h1)
'''
'''
#delete_by_pos function
h1=Node(1)
insert(h1,17,1)
insert(h1,18,2)
insert(h1,19,3)
insert(h1,8,2)
insert(h1,20,4)
insert(h1,10,10)
display(h1)
h1=delete_by_pos(h1,5)  #Deleting tail
display(h1)
h1=delete_by_pos(h1,2)  #Deleting an index other than tail or head
display(h1)
h1=delete_by_pos(h1,12) #Deleting invalid index
display(h1)
h1=delete_by_pos(h1,0)  #Deleting position 0 element
display(h1)
'''


'''
#Appendnode function,length function and display function

head=Node(1)
th=head
for i in range(2,6):
    th.next=Node(i)
    th=th.next
appendnode(head,6)
print('length is ',length(head))
print('calling printRev function')
display(head)

'''

'''
# Linear search function
h=Node(8)
th=h
for i in range(2,6):
    th.next=Node(i)
    th=th.next
display(h)
result=linearSearch(h,5)
if result==True:
    print('Element is present in linked list')
else:
    print('Element is not present in linked list')
'''
'''
#Sorting: mergeSort function

h1=Node(1)
appendnode(h1,-222)
appendnode(h1,156153)
appendnode(h1,124)
appendnode(h1,132)
appendnode(h1,1323)
appendnode(h1,124)
appendnode(h1,-2)
print('Before sorting')
display(h1)
print("Calling mergesort function")
h1=mergeSort(h1)
print('After sorting ')
display(h1)
'''
'''
#Finding middle element
h1=Node(1)
appendnode(h1,2)
appendnode(h1,113)
appendnode(h1,124)
appendnode(h1,13)
appendnode(h1,1224)
appendnode(h1,132)
appendnode(h1,1322)
print(middle(h1,False).data,' This should print 13 because linked list is even and flag is false, so print (n/2)th element i.e 4th element ( starting at 0 based indexing )')
print(middle(h1,True).data, ' This should print 124 because linked list is even and flag is true, so print (n/2-1)th element i.e 3th element ( starting at 0 based indexing )')
'''
'''
# Reversing a linked list
h=Node(1)
for i in range(2,7):
    appendnode(h,i)
print("Before reversing")
display(h)
print("After reversing")
h=reverse(h)
display(h)
'''
'''
# Merging two sorted linked lists : Original linked lists are modified
h1=Node(1)
appendnode(h1,2)
appendnode(h1,13)
appendnode(h1,124)
h2=Node(5)
appendnode(h2,16)
appendnode(h2,71)
appendnode(h2,181)
appendnode(h2,202)
print('h1 is ')
display(h1)
print('h2 is ')
display(h2)
h1=merge(h1,h2)
print('h1 after sorting ')
display(h1)
'''
