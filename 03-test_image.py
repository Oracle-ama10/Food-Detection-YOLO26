from ultralytics import YOLO

# โหลดโมเดลที่ผ่านการฝึก (Trained Model)
model = YOLO("best.pt")

# นำโมเดลไปทดสอบกับรูปภาพ
results = model.predict(
    "test/test_01.jpg",    # ชื่อไฟล์รูปภาพที่ต้องการทดสอบ เช่น "coffee.jpg"
    conf=0.7,       # กำหนดค่า Confidence ขั้นต่ำที่ 50%
    save=True       # บันทึกภาพผลลัพธ์ที่ตรวจจับได้
)

# แสดงผลลัพธ์การตรวจจับของรูปภาพแรก
results[0].show()