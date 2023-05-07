import os
import random

# Đường dẫn tới thư mục chứa các file input
input_dir = "input"

# Tạo thư mục nếu nó chưa tồn tại
if not os.path.exists(input_dir):
    os.mkdir(input_dir)

# Số lượng bộ test case
start_test_cases = 29
end_test_cases = 30

# Phạm vi giá trị của n
min_n = 99999
max_n = 100000

# Phạm vi giá trị của a và b
min_value = 1
max_value = 10**9

# Tạo các file input
for i in range(start_test_cases, end_test_cases):
    # Tên file input
    input_filename = f"{input_dir}/input{i}.inp"
    
    # Tạo n và các cặp giá trị a và b ngẫu nhiên
    # n = random.randint(min_n, max_n)
    n = 0
    value = []
    end_last = 1
    while(True):
        start_value = end_last
        end_value = random.randint(start_value + 1, start_value + 100 + 1)
        value.append((start_value, end_value))
        n = n + 1
        end_last = end_value
        if n == 10**6:
            break
        
    # Ghi dữ liệu vào file input
    with open(input_filename, "w") as f:
        # Ghi giá trị của n
        f.write(f"{n}\n")
        
        # Ghi các cặp giá trị a và b
        for a, b in value:
            f.write(f"{a} {b}\n")
