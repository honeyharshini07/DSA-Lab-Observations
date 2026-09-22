def _init_ (self,size):
    self.size=size
    self.queue=[None]*size
    self.front=-1
    self.rear=-1
def enqueue(self,x):
    if self.rear==self.size-1:
        print("Queue overflowed")
    else:
        if self.front==-1:
            self.front=0
        self.rear=+1
        self.queue[self.rear]=x
        print(f"{x} is inserted into the queue.")
