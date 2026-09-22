def dequeue(self):
    if self.front==-1 or self.front>self.rear:
        print("Underflow of queue")
    else:
        x=self.queue[self.front]
        self.queue[self.front]=None
        self.front+=1
        print(f"{x} is deleted from queue")
        if self.front>self.rear:
            self.front=-1
            self.rear=-1
        
        
