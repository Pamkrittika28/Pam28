class CircularQueue:
    def __init__(self, n):
        self.n = n
        self.queue = [ ] * n
        self.front = -1
        self.rear = -1


    def enqueue(self, data):
        if((self.rear+1)%self.n==self.front):
            print('เพิ่มข้อมูลไม่ได้เพราะคิวในวงกลมเต็ม')
        elif(self.front==-1):
            self.front=0
            self.rear=0
            self.queue.append(data)
        else:
            self.rear+(self.rear+1)%self.n
            self.queue.append(data)

    def dequeue(self):
        if(self.front==-1):
            print('ลบข้อมูลไม่ได้เพราะคิววงกลมว่าง')
        elif(self.front==self.rear):
            self.front=-1
            self.rear=-1
        else:
            self.queue[self.front] =None
            self.front =(self.front+1)% self.n
        

    def display(self):
        if(self.front==-1):
            print('แสดงข้อมูลไม่ได้เพราะคิววงกลมว่าง')
        elif(self.rear>=self.front):
            for i in range(self.front,self.rear+1):
                print(self.queue[i])
        else:
            for i in range(0,self.rear+1):
                print(self.queue[i])





n=int(input('โปรดระบุขนาดของคิววงกลมที่มีขนาดตั้งแต่ 5 ช่องขึ้นไป = '))
while n < 5:
    n=int(input('โปรดระบุขนาดของคิววงกลมที่มีขนาดตั้งแต่ 5 ช่องขึ้นไป = '))
q = CircularQueue(n)

print("โปรดระบุทางเลือกในการดำเนินการใน:")
print("1 รับข้อมูลตัวเลขจำนวนเต็มเพื่อเก็บในคิววงกลม:")
print("2 ลบข้อมูลที่จัดเก็บในคิววงกลม 1 ตัว:")
print("3 แสดงตัวเลขจำนวนเต็มที่มีค่าน้อยกว่า 150 ที่เก็บในคิววงกลมทางจอภาพ:")


manu=input('ป้อนตัวเลือก(1/2/3):')
while manu=='1' or manu=='2' or manu=='3':
    if manu=='1':
        data=int(input("ป้อนข้อมูลตัวเลข:"))
        q.enqueue(data)
    elif manu=='2':
        q.dequeue()
    elif manu=='3':
        q.display()
    else:
        print('ตัวเลือกไม่ถูกต้องกรุณาลองใหม่')

    manu=input('ป้อนตัวเลือก(1/2/3):')


