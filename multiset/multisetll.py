from node import *

# A class implementing Multiset as a linked list.

class Multiset:

    def __init__(self):
        """
        Produces a newly constructed empty Multiset.
        __init__: -> Multiset
        Field: _head points to the first node in the linked list
        """
        self._head = None


    def empty(self):
        """
        Checks emptiness of Multiset.
        empty: Multiset -> Bool
        :return: True if Multiset is empty and False otherwise.
        """

        return self._head == None

    def __contains__(self, value):
        """
        Checks existence of value in the Multiset.
        __contains__: Multiset Any -> Bool
        :param value: the value to be check.
        :return: True if Multiset is in the Multiset and False otherwise.
        """
        current = self._head
        while current != None:
            if current.item == value:
                return True
            else:
                current = current.next
                #!!!!!!!!!!!!!!!!!!!
        return False

    def add(self, value):
        """
        Adds the value to multiset.

        :param value: the value to be added.
        """
        if self._head is None:
            self._head = Node(value)
        else:
            rest = self._head
            self._head = Node(value)
            self._head.counts = rest

    def delete(self, value):
        """

        :param value: value first occurrence of which should be deleted.
        """
        current = self._head
        previous = None
        while current is not None and current.item != value:
            previous = current
            current = current.counts
        if current is not None:
            if previous is None:
                self._head = self._head.counts
            else:
                previous.count = current.counts
    def remove_all(head):#!?!?!?
        for i in head:
            self.delete(i)
    def split_half(head):
        x = head
        k = 0
        while x is not None:
            k+=1
            x = x.counts
        p = 0
        while k//2 == p:
            p +=1
            parth1 = x
            x = x.counts
        parth2 = x
        return parth1,parth2

    def __str__(self):
        str = ""
        x = self._head
        while x is not None:
            str+=str(x.data)
            x = x.counts
        return str
if __name__ == "__main__":
    a = Multiset()

    n1 = Node(3)
    n2 = Node("CS@UCU")
    n3 = Node("Arman")
    n4 = Node("Our leader")
    ##################
    a.add(n1)
    a.add(n2)
    a.add(n3)
    a.add(n4)
    ##################
    
    n1.next = n2
    n2.next = n3
    n3.next = n4
    x = n1
    while x != None:
        print(x.data,end="-->")
        x = x.next
    #print(x)