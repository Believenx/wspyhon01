def calculate_grass_cutting_cost(width, length, price_per_sqm):
    area = width * length
    total_cost = area * price_per_sqm
    return total_cost

def main():
    # รับค่าความกว้างและความยาวของสนามหญ้า
    width = float(input("โปรดป้อนความกว้างของสนามหญ้า (เมตร): "))
    length = float(input("โปรดป้อนความยาวของสนามหญ้า (เมตร): "))

    # ราคาตัดหญ้าต่อตารางเมตร
    price_per_sqm = float(input("โปรดป้อนราคาตัดหญ้าต่อตารางเมตร (บาท): "))

    # คำนวณราคาค่าตัดหญ้าที่ต้องจ่าย
    total_cost = calculate_grass_cutting_cost(width, length, price_per_sqm)

    print("ราคาค่าตัดหญ้าที่ต้องจ่ายคือ:", total_cost, "บาท")

if __name__ == "__main__":
    main()
