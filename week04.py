class Node:
    def __init__(self,data,link=None):
        self.data = data
        self.link = link
    #a = Node("ABC")
class Linkedlist:
    def __init__(self):
        self.head = None

    def append(self,data):
        if not self.head:
            self.head
            return
        current = self.head
        while current.link:
            current = current.link
        current.link = Node(data)

ll = Linkedlist()
ll.append(8)
ll.append(10)
ll.append(-9)


