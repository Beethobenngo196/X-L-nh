from ultralytics import YOLO

# Load mô hình đã huấn luyện
model = YOLO(r'D:\XLA1\runs\detect\Ket_Qua_Train\lan_chay\weights\best.pt')

 
results = model.predict(source=r'D:\XLA1\data\input\test.mp4', save=True, conf=0.25)


# In kết quả
for r in results:
    print(r.boxes) # In các box phát hiện được
