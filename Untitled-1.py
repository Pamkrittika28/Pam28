class Node:
    def __init__(self):
        self.data = None
        self.leftChild = None
        self.rightChild = None

    def insert(self, data):
        self.data = data
        if data > 0:  
            left_data = int(input(f'โปรดป้อนจำนวนหมายเลขของโหนด leftChild ของ {self.data} (ถ้าไม่มีให้ป้อนจำนวนเต็มที่มีค่าน้อยกว่าหรือเท่ากับ 0): '))
            if left_data > 0:
                self.leftChild = Node()
                self.leftChild.insert(left_data)
            
            right_data = int(input(f'โปรดป้อนจำนวนหมายเลขของโหนด rightChild ของ {self.data} (ถ้าไม่มีให้ป้อนจำนวนเต็มที่มีค่าน้อยกว่าหรือเท่ากับ 0): '))
            if right_data > 0:
                self.rightChild = Node()
                self.rightChild.insert(right_data)
    
    def pre_order(self, tree):
        if tree:
            if tree.data % 2 == 0:
                print(tree.data)
            self.pre_order(tree.leftChild)
            self.pre_order(tree.rightChild)
                 
    def in_order(self, tree):
        if tree:
            self.in_order(tree.leftChild)
            if tree.data < 150:
                print(tree.data)
            self.in_order(tree.rightChild)
           
    def post_order(self, tree):
        if tree:
            self.post_order(tree.leftChild)        
            self.post_order(tree.rightChild)
            if tree.data % 7 == 0:
                print(tree.data)


# Create the root node
Pam = Node()

# Input root data
data = int(input('โปรดป้อนจำนวนเต็มเพื่อจัดเก็บที่ root node: '))
Pam.insert(data)

# Menu for traversal choices
print("โปรดระบุทางเลือกในการดำเนินการ:")
print("1 ท่องไปในต้นไม้ทวิภาคแบบ Pre-order และแสดงจำนวนเต็มที่จัดเก็บในแต่ละโหนดที่เป็นเลขคู่ทางจอภาพ")
print("2 ท่องไปในต้นไม้ทวิภาคแบบ In-order และแสดงจำนวนเต็มที่จัดเก็บในแต่ละโหนดที่มีค่าน้อยกว่า 150 ทางจอภาพ")
print("3 ท่องไปในต้นไม้ทวิภาคแบบ Post-order และแสดงจำนวนเต็มที่จัดเก็บในแต่ละโหนดที่หารด้วย 7 ลงตัวทางจอภาพ")

# Get the user's choice
choice = input('ป้อนทางเลือกในการดำเนินการ (1/2/3): ').strip()
if choice == '1':
    print("Pre-order (ตัวเลขที่เป็นเลขคู่):")
    Pam.pre_order(Pam)
elif choice == '2':
    print("In-order (ตัวเลขที่มีค่า <150):")
    Pam.in_order(Pam)
elif choice == '3':
    print("Post-order (ตัวเลขที่หารด้วย 7 ลงตัว):")
    Pam.post_order(Pam)
else:
    print("ตัวเลือกไม่ถูกต้อง.")
