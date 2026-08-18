"""
โปรแกรมคำนวณกำไรจากการขายของออนไลน์ (Online Profit Calculator)
ภาษา: Python 3
"""

def calculate_profit(cost_price, selling_price, quantity, shipping_fee=0.0, platform_fee_percent=0.0, other_costs=0.0):
    """
    คำนวณกำไรและสรุปค่าใช้จ่ายทั้งหมด
    """
    total_revenue = selling_price * quantity
    total_cost_goods = cost_price * quantity
    total_platform_fee = (total_revenue * platform_fee_percent) / 100.0
    total_expenses = total_cost_goods + shipping_fee + total_platform_fee + other_costs
    net_profit = total_revenue - total_expenses
    profit_per_item = net_profit / quantity if quantity > 0 else 0.0
    profit_margin = (net_profit / total_revenue * 100.0) if total_revenue > 0 else 0.0

    return {
        "total_revenue": total_revenue,
        "total_cost_goods": total_cost_goods,
        "total_platform_fee": total_platform_fee,
        "total_expenses": total_expenses,
        "net_profit": net_profit,
        "profit_per_item": profit_per_item,
        "profit_margin": profit_margin
    }

def main():
    print("=" * 45)
    print(" 💸 โปรแกรมคำนวณกำไรจากการขายของออนไลน์")
    print("=" * 45)

    try:
        cost_price = float(input("1. ราคาทุนสินค้าต่อชิ้น (บาท): ") or 0)
        selling_price = float(input("2. ราคาขายสินค้าต่อชิ้น (บาท): ") or 0)
        quantity = int(input("3. จำนวนสินค้าที่ขายได้ (ชิ้น): ") or 0)
        shipping_fee = float(input("4. ค่าจัดส่งรวมทั้งหมด (บาท) [กด Enter หากไม่มี]: ") or 0)
        platform_fee_percent = float(input("5. ค่าธรรมเนียมแพลตฟอร์ม (%) [กด Enter หากไม่มี]: ") or 0)
        other_costs = float(input("6. ค่าใช้จ่ายอื่นๆ รวม (ยิงแอด/กล่อง) (บาท) [กด Enter หากไม่มี]: ") or 0)

        res = calculate_profit(cost_price, selling_price, quantity, shipping_fee, platform_fee_percent, other_costs)

        print("\n" + "=" * 45)
        print(" 📊 สรุปผลการคำนวณ")
        print("=" * 45)
        print(f" ยอดขายรวมทั้งหมด : {res['total_revenue']:,.2f} บาท")
        print(f" - ทุนสินค้ารวม  : {res['total_cost_goods']:,.2f} บาท")
        print(f" - ค่าธรรมเนียมแอป : {res['total_platform_fee']:,.2f} บาท")
        print(f" - ค่าส่ง + อื่นๆ   : {(shipping_fee + other_costs):,.2f} บาท")
        print("-" * 45)
        print(f" รวมค่าใช้จ่ายทั้งหมด: {res['total_expenses']:,.2f} บาท")
        print("-" * 45)
        
        status = "กำไรสุทธิ" if res['net_profit'] >= 0 else "ขาดทุนสุทธิ"
        print(f" 🎯 {status}    : {res['net_profit']:,.2f} บาท")
        print(f" 📦 เฉลี่ยต่อชิ้น    : {res['profit_per_item']:,.2f} บาท")
        print(f" 📈 อัตรากำไร (Margin): {res['profit_margin']:.2f}%")
        print("=" * 45)

    except ValueError:
        print("\n❌ กรุณากรอกตัวเลขให้ถูกต้อง!")

if __name__ == "__main__":
    main()