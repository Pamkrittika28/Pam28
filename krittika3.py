class Node:
    def __init__(self, info=None):
        self.info = info
        self.next = None

class SLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def AtTheBeginning(self, data):
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
        print("ข้อมูลใน Singly linked list คือ")
        current = self.head
        while current is not None:
            print(current.info)
            current = current.next
        print(F"ข้อมูลที่จัดเก็บในตำแหน่งพ้อยเตอร์ head ชี้คือ {self.head.info}")
        print(F"ข้อมูลที่จัดเก็บในตำแหน่งพ้อยเตอร์ head ชี้คือ {self.head.info}")
        

        current=self.head
        total=0
        count=0
        while current :
            total += current.info
            count += 1
            current = current.next
        average = total / count
        print(F"ค่าเฉลี่ยของข้อมูลที่เก็บใน ingly linked list คือ {average:.2f}")
        
        

   

linked_list = SLinkedList()

print("โปรดระบุทางเลือกในการดำเนินการกับ Singly linked list:")
print("B : เพิ่มข้อมูลที่จุดเริ่มต้นของ Singly linked list:")
print("E : เพิ่มข้อมูลแบบต่อจากโหนดสุดท้ายของ Singly linked list:")


while  True :
    manu = input('ป้อนตัวเลือก(B/E):')
    if manu == 'B':
        data = int(input("ตัวเลขที่ต้องการเพิ่ม:"))
        linked_list.AtTheBeginning(data)
    elif manu == 'E':
        data = int(input("ตัวเลขที่ต้องการเพิ่ม:"))
        linked_list.AtTheEnd(data)
    else:
        break
        
linked_list.display()  

   


