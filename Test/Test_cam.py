from ultralytics import YOLO

# Load mô hình đã huấn luyện
model = YOLO(r'D:\XLA1\runs\detect\Ket_Qua_Train\lan_chay\weights\best.pt')

# Chạy dự đoán từ webcam và hiển thị trực tiếp (show=True)
results = model.predict(source=r'0', show=True, conf=0.8)

# In kết quả
for r in results:
    print(r.boxes) # In các box phát hiện được