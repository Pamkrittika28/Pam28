class CircularQueue:
    def __init__(self, n):
        self.n = n
        self.queue = [None] * n  # ใช้ None เพื่อเป็นตัวแทนที่ว่าง
        self.front = -1
        self.rear = -1

    def enqueue(self, data):
        if (self.rear + 1) % self.n == self.front:
            print('เพิ่มข้อมูลไม่ได้เพราะคิวในวงกลมเต็ม')
        elif self.front == -1:
            self.front = 0
            self.rear = 0
            self.queue[self.rear] = data  # เพิ่มข้อมูลที่ตำแหน่ง rear
        else:
            self.rear = (self.rear + 1) % self.n
            self.queue[self.rear] = data  # เพิ่มข้อมูลที่ตำแหน่ง rear
        print(f'เพิ่มข้อมูล {data} ลงในคิว')

    def dequeue(self):
        if self.front == -1:
            print('ลบข้อมูลไม่ได้เพราะคิววงกลมว่าง')
            return None
        elif self.front == self.rear:
            temp = self.queue[self.front]
            self.front = self.rear = -1  # คิวว่างหลังจากลบข้อมูล
        else:
            temp = self.queue[self.front]
            self.front = (self.front + 1) % self.n
        print(f'ลบข้อมูล {temp} จากคิว')
        return temp

    def display(self):
        if self.front == -1:
            print('แสดงข้อมูลไม่ได้เพราะคิววงกลมว่าง')
        elif self.rear >= self.front:
            for i in range(self.front, self.rear + 1):
                print(self.queue[i], end=' ')
            print()  # ขึ้นบรรทัดใหม่
        else:
            for i in range(self.front, self.n):
                print(self.queue[i], end=' ')
            for i in range(0, self.rear + 1):
                print(self.queue[i], end=' ')
            print()  # ขึ้นบรรทัดใหม่

    def display_above_150(self):
        if self.front == -1:
            print('คิววงกลมว่าง ไม่มีข้อมูลให้แสดง')
        else:
            print("ข้อมูลที่มีค่าน้อยกว่า 150:")
            if self.rear >= self.front:
                for i in range(self.front, self.rear + 1):
                    if self.queue[i] < 150:
                        print(self.queue[i], end=' ')
                print()
            else:
                for i in range(self.front, self.n):
                    if self.queue[i] < 150:
                        print(self.queue[i], end=' ')
                for i in range(0, self.rear + 1):
                    if self.queue[i] < 150:
                        print(self.queue[i], end=' ')
                print()


# รับขนาดของคิววงกลม
n = int(input('โปรดระบุขนาดของคิววงกลมที่มีขนาดตั้งแต่ 5 ช่องขึ้นไป = '))
while n < 5:
    n = int(input('โปรดระบุขนาดของคิววงกลมที่มีขนาดตั้งแต่ 5 ช่องขึ้นไป = '))

# สร้างคิววงกลม
queue = CircularQueue(n)

while True:
    print("\nโปรดระบุทางเลือกในการดำเนินการใน:")
    print("1 รับข้อมูลตัวเลขจำนวนเต็มเพื่อเก็บในคิววงกลม:")
    print("2 ลบข้อมูลที่จัดเก็บในคิววงกลม 1 ตัว:")
    print("3 แสดงตัวเลขจำนวนเต็มที่มีค่าน้อยกว่า 150 ที่เก็บในคิววงกลมทางจอภาพ:")

    manu = input('ป้อนตัวเลือก(1/2/3): ')

    if manu == '1':
        data = int(input("ป้อนข้อมูลตัวเลข: "))
        queue.enqueue(data)
    elif manu == '2':
        queue.dequeue()
    elif manu == '3':
        queue.display_above_150()
    else:
        print('ตัวเลือกไม่ถูกต้องกรุณาลองใหม่')
