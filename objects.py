class Stack:
    def __init__(self, cap):
        self.cap = cap
        self.top = -1
        self.a = [0] * cap

    def push(self, x):
        if self.top >= self.cap - 1:
            #print("Stack Overflow")
            return False
        self.top += 1
        self.a[self.top] = x
        return True

    def pop(self):
        if self.top < 0:
            #print("Stack Underflow")
            return 0
        popped = self.a[self.top]
        self.top -= 1
        return popped

    def peek(self):
        if self.top < 0:
            #print("Stack is Empty")
            return 0
        return self.a[self.top]

    def is_empty(self):
        return self.top < 0

class Queue():

    def __init__(self, k):
        self.k = k
        self.queue = [None] * k
        self.head = self.tail = -1

    # Insert an element into the circular queue
    def enqueue(self, data):

        if ((self.tail + 1) % self.k == self.head):
            print("The circular queue is full\n")

        elif (self.head == -1):
            self.head = 0
            self.tail = 0
            self.queue[self.tail] = data
        else:
            self.tail = (self.tail + 1) % self.k
            self.queue[self.tail] = data

    # Delete an element from the circular queue
    def dequeue(self):
        if (self.head == -1):
            print("The circular queue is empty\n")

        elif (self.head == self.tail):
            temp = self.queue[self.head]
            self.head = -1
            self.tail = -1
            return temp
        else:
            temp = self.queue[self.head]
            self.head = (self.head + 1) % self.k
            return temp