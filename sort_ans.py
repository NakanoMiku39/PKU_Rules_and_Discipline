import json
import re

input_file = 'ans.json'
output_file = 'ans.json'  # 如需另存为新文件可改名

# 读取文件
with open(input_file, 'r', encoding='utf-8') as f:
    data = json.load(f)

unique = {}
for item in data:
    # 去掉题目前面的题号（如 '4.'）
    # 支持数字加点后面可能有空格
    item['content'] = re.sub(r'^\s*\d+\.\s*', '', item['content'])
    if item["id"] not in unique:
        unique[item["id"]] = item

result = sorted(unique.values(), key=lambda x: x["id"])

with open(output_file, 'w', encoding='utf-8') as f:
    json.dump(result, f, ensure_ascii=False, indent=2)

print(f'处理完成，已写入 {output_file}')
