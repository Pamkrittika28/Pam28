class Node:
    def __init__(self):
        self.data = None
        self.leftChild = None
        self.rightChild = None

    def insert(self,data):
        self.data = data 
        if data > 0:  
            data = int(input(f'โปรดป้อนจำนวนหมายเลขของโหนด leftChild ของ {self.data}(ถ้าไม่มีให้ป้อนจำนวนเต็มที่มีค่าน้อยกว่าหรือเท่ากับ 0):'))
            self.leftChild = Node()
            self.leftChild.insert(data)      
        if data > 0:
            data = int(input(f'โปรดป้อนจำนวนหมายเลขของโหนด rightChild ของ {self.data}(ถ้าไม่มีให้ป้อนจำนวนเต็มที่มีค่าน้อยกว่าหรือเท่ากับ 0):'))
            self.rightChild = Node()
            self.rightChild.insert(data)
    
    def PreOrder(self, tree):
        if tree:
            if tree.data % 2 == 0:
                print(self.data, end=' ')
            self.PreOrder(tree.leftChild)
            self.PreOrder(tree.rightChild)
                 
    def InOrder(self, tree):
        if tree:
            self.InOrder(tree.leftChild)
            if tree.data <150:
                print(self.data, end=' ')               
            self.InOrder(tree.rightChild)
           
    def PostOrder(self, tree):
        if tree:
            self.PostOrder(tree.leftChild)        
            self.PostOrder(tree.rightChild)
            if tree.data % 7 == 0:
               print(self.data, end=' ')


Pam = Node()


data=int(input('โปรดป้อนจำนวนเต็มเพื่อจัดเก็บที่ root node:'))

Pam.insert(data)


print("โปรดระบุทางเลือกในการดำเนินการใน:")
print("1 ท่องไปในต้นไม้ทวิภาคแบบ Pre-order และแสดงจำนวนเต็มที่จัดเก็บในแต่ละโหนดที่เป็นเลขคู่ทางจอภาพ:")
print("2 ท่องไปในต้นไม้ทวิภาคแบบ In-order และแสดงจำนวนเต็มที่จัดเก็บในแต่ละโหนดที่มีค่าน้อยกว่า 150 ทางจอภาพ:")
print("2 ท่องไปในต้นไม้ทวิภาคแบบ Post-order และแสดงจำนวนเต็มที่จัดเก็บในแต่ละโหนดที่หารด้วย 7 ลงตัวทางจอภาพ:")


choice = input('ป้อนทางเลือกในการดำเนินการ (1/2/3): ')
if choice == '1':
    print("Pre-order (ตัวเลขที่เป็นเลขคู่):")
    root.pre_order()
    print() 

elif choice == '2':
    print("In-order (ตัวเลขที่มีค่า < 150):")
    root.in_order()
    print()

elif choice == '3':
    print("Post-order (ตัวเลขที่หารด้วย 7 ลงตัว):")
    root.post_order()
    print()

else:
    print("ตัวเลือกไม่ถูกต้อง.")

