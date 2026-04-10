import cv2
import os
import numpy as np
from ultralytics import YOLO

def FrameCapture(video_path, output_folder):   
    os.makedirs(output_folder, exist_ok=True)
    video = cv2.VideoCapture(video_path) # Mở video từ đường dẫn đã cho
    if not video.isOpened():
        print(f"❌ LỖI: Không thể mở video tại '{video_path}'. Hãy kiểm tra lại đường dẫn!")
        return
    count = 0 
    saved_count = 0
    
    while True: 
        success, image = video.read()
        
        if not success:
            break  
            
        if count % 10 == 0:
            file_name = f"frame_{saved_count}.jpg" # Tên file theo số thứ tự của ảnh đã lưu
            save_path = os.path.join(output_folder, file_name) # Tạo đường dẫn đầy đủ để lưu ảnh
            
            cv2.imwrite(save_path, image) # Lưu ảnh vào thư mục đã chỉ định
            print(f"✅ Đã lưu: {save_path}")
            saved_count += 1 #Cứ mỗi 10 frames mới lưu một ảnh, nên chỉ tăng saved_count khi thực sự lưu ảnh
            
        count += 1 
    video.release()
    print(f"🎉 Hoàn tất! Đã trích xuất {saved_count} ảnh vào thư mục '{output_folder}'.")

if __name__ == "__main__":
    duong_dan_video = os.path.join("data", "input", "test.mp4") 
    thu_muc_luu_anh = os.path.join("data","dataset", "output", "frames") 
    
    FrameCapture(duong_dan_video, thu_muc_luu_anh)
# Cắt 400 frames bỏ vào D:\XLA1\data\dataset\test\images 
# Cắt 200 frams bỏ vào D:\XLA1\data\dataset\train\images 
