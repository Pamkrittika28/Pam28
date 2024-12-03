def isEmpty (pamStack):
    if len(pamStack) == 0:
        print('Stack is empty')
        return 1
    else:
        return 0

def isFull (pamStack):
    if len(pamStack)== n:
        print('Stack is full')
        return 1
    else:
        return 0

def display_menu ():
    print("โปรดระบุทางเลือกในการดำเนินการใน Stack:")
    print("1. เพิ่มข้อมูลใน Stack")
    print("2. ลบข้อมูลจาก Stack")
    print("3. แสดงข้อมูลทั้งหมดที่เก็บไว้ใน Stack")
    print("4. แสดงข้อมูลที่จัดเก็บใน Stack")
    p=int(input("ทางเลือกในการดำเนินการ = "))

def push_Satack (item,pamStack) :
    test = isFull(pamStack)
    if test == 1:
        print("จัดเก็บข้อมูลไม่ได้เพราะ Stack เต็ม")
    else:
        pamStack.append(item)

def pop_Satack (pamStack):
    test= isEmpty (pamStack)
    if test == 1:
        print("ลบข้อมูลไม่ได้เพราะ Stack ว่าง")
    else:
        pamStack.pop()


def display_Stack (pamStack):
    test= isEmpty (pamStack)
    if test == 1:
        print("แสดงข้อมูลใน Stack ไม่ได้เพราะ Stack ว่าง")
    else:
        print(pamStack)

def calculate_average (pamStack):
    if not is_empty ():
        average = sum(pamStack) / len(pamStack)
        print("ค่าเฉลี่ยของข้อมูลใน Stack คือ; {average:.2F}")
    else:
        print("แสดงค่าข้อมูลใน Stack ไม่ได้เพราะ Stack ว่าง")





n=int(input('โปรดระบุขนาดของ Stack ที่มีขนาดตั้งแต่ 6 ช่องขึ้นไป = '))
while n < 6:
    n=int(input('โปรดระบุขนาดของ Stack ที่มีขนาดตั้งแต่ 6 ช่องขึ้นไป = '))
pamStack = []*n

