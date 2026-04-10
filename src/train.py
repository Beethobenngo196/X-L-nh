from ultralytics import YOLO
import os

if __name__ == '__main__':
    # File này sẽ tự động tải về thư mục gốc nếu chưa có
    model = YOLO("yolov8n.pt") 

    resutlts = model.train(
        data="data/Data.yaml",   
        epochs=50,               
        imgsz=640,  
        workers=0,             
        batch=8,                  
        device=0,                                 
        project="Ket_Qua_Train",  # Thư mục lưu kết quả
        name="lan_chay",
        exist_ok=True             # Ghi đè nếu tên thư mục đã tồn tại
    )