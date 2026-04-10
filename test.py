# Cách bạn làm (import tọa độ lại vào makesense.ai, đổi tên, rồi export) là CHUẨN.
# Chạy script dưới đây để kiểm tra lại thư mục gộp cuối cùng xem có xót label lạ nào không:

import glob
import os

# Đường dẫn tới folder chứa tất cả 600 file .txt đã gộp
folder_path = r"./C:\Users\ngovu\Downloads\labels_my-project-name_2026-04-06-12-30-24\*.txt" 
# Các label hợp lệ (0, 1, 2, 3)
valid_labels = {'0', '1', '2', '3'} 

error_count = 0

for file_path in glob.glob(folder_path):
    if os.path.basename(file_path) == "classes.txt":
        continue
        
    with open(file_path, "r") as f:
        for line_num, line in enumerate(f, 1):
            parts = line.strip().split()
            if not parts: 
                continue
            
            class_id = parts[0]
            if class_id not in valid_labels:
                print(f"Lỗi tại file {os.path.basename(file_path)} - Dòng {line_num}: Chứa nhãn lạ '{class_id}'")
                error_count += 1

if error_count == 0:
    print("Hoàn hảo! Dữ liệu đã chuẩn và đồng nhất, sẵn sàng train.")