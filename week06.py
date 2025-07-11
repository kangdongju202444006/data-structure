class Node:
    def __init__(self, data, link=None):
        self.data = data
        self.link = link


class Queue:
    def __init__(self):
        self.front = None
        self.rear = None
        self.size = 0

    def enqueue(self, data):
        self.size = self.size + 1
        node = Node(data)

        if self.rear is None:
            self.front = node
            self.rear = node
        else:
            self.rear.link = node
            self.rear = node  # move


    def dequeue(self):
        if self.front is None:
            raise IndexError("Queue is empty!")
        self.size = self.size - 1
        temp = self.front
        self.front = self.front.link  # move
        if self.front is None:
            self.rear = None
        return temp.data


q = Queue() #새로운 queue의 객체를 생성
q.enqueue("Data structure") #데이터를 큐에 삽입
q.enqueue("Database")
print(q.size, q.front.data, q.rear.data)
print(q.dequeue())
print(q.size, q.front.data, q.rear.data)
print(q.dequeue())
print(q.size, q.front, q.rear)