
class Node:
    def __init__(self,data=None,next=None):
        self.data=data
        self.next=next
class linkedlist:
    def __init__(self):
        self.head = None
    def insert_ata_beg(self,data):
        node = Node(data,self.head)
        self.head=node
    def print(self):
        if self.head is None:
            print("linked is empty")
            return
        itr = self.head
        llstr=''
        while itr:
            llstr = llstr + str(itr.data)+"-->"
            itr = itr.next
        print(llstr)
    def insert_at_end(self,data):
        if self.head is None:
            self.head = Node(data,None)
            return
        itr = self.head
        while itr.next:
            itr = itr.next
        itr.next = Node(data,None)
    def insert_values(self,data_list):
        self.head = None
        for i in data_list:
            self.insert_at_end(i)
    def get_length(self):
        count =0
        itr = self.head
        while itr:
            count = count + 1
            itr = itr.next
        return count

    def remove_at(self,n):
        if n < 0 or n > self.get_length():
            raise Exception("invalid")
        if n==0:
            self.head = self.head.next
            return
        count = 0
        itr = self.head
        while itr:
            if count == n-1:
                itr.next = itr.next.next
                break
            itr = itr.next
            count = count + 1
    def insert_at(self,n,data1):
        if n==0:
            self.insert_ata_beg(data1)
            return
        count = 0
        itr =  self.head
        while itr:
            if count == n-1:
                node = Node(data1,itr.next)
                itr.next = node
                break
            itr = itr.next
            count = count + 1
    def insert_after_value(self,data_after,data_to_insert):
        if data_after == self.head:
            self.next.insert_ata_beg(data_to_insert)
            return
        count = 0
        itr = self.head
        while itr:
            if itr.data == data_after:
                node = Node(data_to_insert,itr.next)
                itr.next = node
                break
            itr = itr.next
            count = count + 1
    def remove_by_value(self,data1):
        if data1 == self.head.data:
            self.head = self.remove_at(0)
            return
        count = 0
        itr = self.head
        while itr:
            if itr.next.data == data1:
                itr.next=itr.next.next
                break
            itr = itr.next
            count = count + 1


if __name__=='__main__':
    ll = linkedlist()
    ll.insert_values(["apple","banana","mango","orange"])
    #ll.insert_ata_beg(5)
    #ll.insert_ata_beg(50)
    #ll.insert_at_end(66)

    ll.print()
    ll.remove_by_value("banana")
    ll.print()
    ll.remove_by_value("apple")
    ll.print()