import tkinter as tk
from tkinter import messagebox
from tkinter import ttk

def calculate_profit():
    try:
        # ดึงค่าจากช่องกรอกข้อมูล (Input)
        product_type = combo_type.get()
        selling_price = float(entry_price.get())
        quantity = int(entry_qty.get())
        product_cost = float(entry_cost.get())
        platform_fee_percent = float(entry_fee.get())
        shipping_paid_by_seller = float(entry_shipping.get())
        ads_cost = float(entry_ads.get())
        packaging_cost = float(entry_pack.get())

        # ส่วนการคำนวณ
        total_revenue = selling_price * quantity
        total_product_cost = (product_cost + packaging_cost) * quantity
        total_platform_fee = total_revenue * (platform_fee_percent / 100)
        total_hidden_cost = total_platform_fee + shipping_paid_by_seller + ads_cost
        total_expenses = total_product_cost + total_hidden_cost
        net_profit = total_revenue - total_expenses
        profit_margin_percent = (net_profit / total_revenue) * 100 if total_revenue > 0 else 0

        # แสดงผลลัพธ์บนหน้าจอ GUI
        lbl_res_type.config(text=f"🧸 ประเภทสินค้า: {product_type}")
        lbl_res_revenue.config(text=f"{total_revenue:,.2f} บาท")
        lbl_res_product_cost.config(text=f"{total_product_cost:,.2f} บาท")
        lbl_res_fee.config(text=f"{total_platform_fee:,.2f} บาท")
        lbl_res_expenses.config(text=f"{total_expenses:,.2f} บาท")
        lbl_res_margin.config(text=f"{profit_margin_percent:.2f}%")
        
        # เปลี่ยนสีพื้นหลังกล่องข้อความตามผลกำไร (เขียวพาสเทล = กำไร / แดงพาสเทล = ขาดทุน)
        if net_profit > 0:
            lbl_res_profit.config(text=f" ✨ กำไรสุทธิ: {net_profit:,.2f} บาท ✨ ", bg="#d4edda", fg="#155724")
        elif net_profit < 0:
            lbl_res_profit.config(text=f" 🎀 ขาดทุนสุทธิ: {abs(net_profit):,.2f} บาท 🎀 ", bg="#f8d7da", fg="#721c24")
        else:
            lbl_res_profit.config(text=" 🍳 เสมอตัว (เท่าทุน) ", bg="#fff3cd", fg="#856404")

    except ValueError:
        messagebox.showerror("ข้อผิดพลาด", "คิ้วท์จัง.. กรอกข้อมูลเป็นตัวเลขให้ครบทุกช่องด้วยน้า 🥺\n(ถ้าไม่มีต้นทุนให้ใส่เลข 0 จ้า)")

# --- สร้างหน้าต่างโปรแกรมหลัก ---
root = tk.Tk()
root.title("Pastel Profit Calculator")
root.geometry("480x720")
root.configure(bg="#edf2f7") # พื้นหลังสีเทาอมฟ้าพาสเทล สบายตา

# สไตล์สำหรับ Combobox พาสเทล
style = ttk.Style()
style.theme_use('default')
style.configure("TCombobox", fieldbackground="#fef9f9", background="#ffdfdf", arrowcolor="#ffb6b6")

# ส่วนหัวโปรแกรม (Header บาร์สีชมพูพาสเทล)
header_frame = tk.Frame(root, bg="#ffdfdf", height=65)
header_frame.pack(fill="x", side="top")
header_frame.pack_propagate(False)

lbl_title = tk.Label(header_frame, text="🎨 เครื่องมือคิดกำไรพาสเทลละมุนใจ", font=("Helvetica", 13, "bold"), bg="#ffdfdf", fg="#8a6d6d")
lbl_title.pack(pady=18)

# ฟังก์ชันช่วยสร้างช่องกรอกข้อมูลแบบพาสเทล
def create_input_field(parent, label_text, default_val="0"):
    frame = tk.Frame(parent, bg="#edf2f7")
    frame.pack(fill="x", padx=40, pady=5)
    
    lbl = tk.Label(frame, text=label_text, font=("Helvetica", 10), bg="#edf2f7", fg="#5a6a85", width=28, anchor="w")
    lbl.pack(side="left")
    
    # ช่องกรอกข้อมูลสีขาวนวล ขอบสีชมพูอ่อน
    entry = tk.Entry(frame, font=("Helvetica", 10), justify="right", width=14, bg="#ffffff", fg="#4a5568", bd=1, relief="solid", highlightthickness=1, highlightbackground="#ffe5e5", highlightcolor="#ffb6b6")
    entry.insert(0, default_val)
    entry.pack(side="right", expand=True, fill="x", ipady=4)
    return entry

# --- ช่องเลือกประเภทสินค้า ---
frame_type = tk.Frame(root, bg="#edf2f7")
frame_type.pack(fill="x", padx=40, pady=6)

lbl_select_type = tk.Label(frame_type, text="🍰 เลือกประเภทสินค้า:", font=("Helvetica", 10), bg="#edf2f7", fg="#5a6a85", width=28, anchor="w")
lbl_select_type.pack(side="left")

categories = ["เสื้อผ้าและแฟชั่น", "เครื่องสำอางและความงาม", "อาหารและเครื่องดื่ม", "อุปกรณ์อิเล็กทรอนิกส์", "ของใช้ในบ้าน", "สินค้าแม่และเด็ก", "อื่นๆ"]
combo_type = ttk.Combobox(frame_type, values=categories, font=("Helvetica", 10), state="readonly", width=12)
combo_type.current(0)
combo_type.pack(side="right", expand=True, fill="x")

# สร้างช่องกรอกข้อมูล
entry_price = create_input_field(root, "🛒 ราคาสินค้าที่ตั้งขาย (บาท):", "")
entry_qty = create_input_field(root, "🍼 จำนวนชิ้นที่ขายได้ (ชิ้น):", "1")
entry_cost = create_input_field(root, "💸 ต้นทุนสินค้าต่อชิ้น (บาท):", "")
entry_fee = create_input_field(root, "🏰 ค่าธรรมเนียมแพลตฟอร์ม (%):", "0")
entry_shipping = create_input_field(root, "🦄 ค่าส่งที่ร้านออกให้ลูกค้า (บาท):", "0")
entry_ads = create_input_field(root, "🔮 ค่าโฆษณา / ยิงแอดรวม (บาท):", "0")
entry_pack = create_input_field(root, "📦 ค่ากล่อง + แพ็คต่อชิ้น (บาท):", "0")

# ปุ่มคำนวณสีฟ้าพาสเทล นุ่มนวลตาน่ากด
btn_calc = tk.Button(root, text="🌸 คำนวณผลลัพธ์ 🌸", font=("Helvetica", 10, "bold"), bg="#d2e9f9", fg="#4a6b82", activebackground="#bce0fd", activeforeground="#4a6b82", bd=0, padx=30, pady=9, cursor="hand2", command=calculate_profit)
btn_calc.pack(pady=15)

# --- โซนแสดงผลลัพธ์ (กรอบสีขาวมนๆ สะอาดตา) ---
frame_res = tk.LabelFrame(root, text=" สรุปรายรับ-รายจ่ายสุดคิ้วท์ ", font=("Helvetica", 9, "bold"), bg="#ffffff", fg="#a0aec0", padx=20, pady=12, bd=1, relief="solid")
frame_res.pack(fill="both", expand=True, padx=40, pady=10)

lbl_res_type = tk.Label(frame_res, text="📂 ประเภทสินค้า: -", font=("Helvetica", 10), bg="#ffffff", fg="#4a5568", anchor="w")
lbl_res_type.pack(fill="x", pady=2)

def create_result_line(parent, label_text):
    frame = tk.Frame(parent, bg="#ffffff")
    frame.pack(fill="x", pady=3)
    lbl = tk.Label(frame, text=label_text, font=("Helvetica", 10), bg="#ffffff", fg="#718096")
    lbl.pack(side="left")
    res = tk.Label(frame, text="- บาท", font=("Helvetica", 10, "bold"), bg="#ffffff", fg="#4a5568")
    res.pack(side="right")
    return res

lbl_res_revenue = create_result_line(frame_res, "🍡 ยอดขายรวมทั้งหมด:")
lbl_res_product_cost = create_result_line(frame_res, "🍡 ต้นทุนสินค้า + ค่าแพ็ค:")
lbl_res_fee = create_result_line(frame_res, "🍡 ค่าธรรมเนียมหักจากระบบ:")
lbl_res_expenses = create_result_line(frame_res, "🍡 รวมค่าใช้จ่ายทั้งหมด:")
lbl_res_margin = create_result_line(frame_res, "📈 อัตรากำไรสุทธิ (Margin):")

# ป้ายแสดงกำไรสุทธิแบบบล็อกสีพาสเทล ละมุนและมองเห็นชัดเจน
lbl_res_profit = tk.Label(frame_res, text=" กำไรสุทธิ: - บาท ", font=("Helvetica", 11, "bold"), bg="#edf2f7", fg="#4a5568", pady=6)
lbl_res_profit.pack(fill="x", pady=8)

# กดปุ่ม Enter บนคีย์บอร์ดเพื่อคำนวณ
root.bind('<Return>', lambda event: calculate_profit())

root.mainloop()
