from ultralytics import YOLO

# Load mô hình đã huấn luyện
model = YOLO(r'D:\XLA1\runs\detect\Ket_Qua_Train\lan_chay\weights\best.pt')

# Chạy dự đoán từ webcam và hiển thị trực tiếp (show=True)
results = model.predict(source=r'D:\XLA1\data\dataset\output\frames\frame_194.jpg', show=True, conf=0.5,save=True)

# In kết quả
for r in results:
    print(r.boxes) # In các box phát hiện được