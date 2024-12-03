class Node:
    def __init__(self, info = None):
       self.info = info
       self.next = None

class SLinkedList:
      def __init__(self):
           self.head = None
           self.tail = None

def AtTheBegining(self, data):
        if  self.head != None:
            NewNode = Node(data)
            NewNode.next = self.head
            self.head = NewNode
        else:
            NewNode = Node(data)
            NewNode.next = None
            self.head = NewNode
            self.tail = NewNode

def AtTheEnd(self, data):
        if self.head == None:
            NewNode = Node(data)
            NewNode.next = None
            self.head = NewNode
            self.tail = NewNode
        else:
            NewNode = Node(data)
            NewNode.next = None
            self.tail.next = NewNode
            self.tail = NewNode

def display(self):
    current=self.head
    while current:
        print(current.value, end="")
        current=current.next
    print()



linked_list=LinkedList()





print("โปรดระบุทางเลือกในการดำเนินการกับ Singly linked list:")
print("B : เพิ่มข้อมูลที่จุดเริ่มต้นของ  Singly linked list:")
print("E : เพิ่มข้อมูลแบบต่อจากโหนดสุดท้ายของ  Singly linked list:")
p=int(input("ทางเลือกในการดำเนินการ = "))

manu=input('ป้อนตัวเลือก(B/E):')
while manu=='B' or manu=='E':
    if manu=='B':
        data=int(input("เพิ่มข้อมูลที่จุดเริ่มต้นของ  Singly linked list:"))
        q.enqueue(data)
    elif manu=='E':
         data=int(input("เพิ่มข้อมูลแบบต่อจากโหนดสุดท้ายของ  Singly linked list:"))
         q.enqueue(data)
    else:
        print('ตัวเลือกไม่ถูกต้องกรุณาลองใหม่')

    manu=input('ป้อนตัวเลือก(B/E):')
