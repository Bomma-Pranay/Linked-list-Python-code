class Node:
    def __init__(self,val):
        self.data=val
        self.next=None

def appendnode(head,val):
    if head==None:
        val=Node(val)
        head=val
        return
    th=head
    while th.next!=None:
        th=th.next
    th.next=Node(val)
    return

def size(head):
    if head is None:
        return 0
    c=0
    th=head
    while th!=None:
        c+=1
        th=th.next
    return c

def insert(h,pos,val):
    x=size(h)
    if pos<0 or pos>x:
        print('invalid')
        return h
    if pos==0:
        val=Node(val)
        val.next=h
        h=val
        return val
    else:
        th=h
        curr_pos=0
        pos-=1
        while pos!=0:
            h=h.next
            pos-=1
        val=Node(val)
        val.next=h.next
        h.next=val
        return th
def display(h):
    if h==None:
        print(None)
        return
    if h.next==None:
        print(h.data)
        return
    th=h
    while th:
        print(th.data,end='->')
        th=th.next
    print()
    return


h=Node(3)
appendnode(h,5)
appendnode(h,16)
appendnode(h,1)
appendnode(h,9)
#display(h)
h=insert(h,2,8)
display(h)
#Converting ll to array for sorting and again reconstructing ll
l=[]
th=h
while th:
    l.append(th.data)
    th=th.next
print(l)
l.sort()
print(l)
new_head=Node(l[0])
for i in range(1,len(l)):
    appendnode(new_head,l[i])
display(new_head)
