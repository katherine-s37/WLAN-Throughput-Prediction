import pandas as pd
import os
folder_path = 'F:/002中国地质大学(北京)数理学院/101竞赛/202409数学建模赛题/算法刺客/B题/train3AP'  # 替换为你的文件夹路径
output_path = 'train3AP.csv'  # 替换为你想保存的文件名
dataframes = []
for filename in os.listdir(folder_path):
    if filename.endswith('.csv'):
        # 构建完整的文件路径
        file_path = os.path.join(folder_path, filename)
        # 读取CSV文件
        df = pd.read_csv(file_path)
        # 将读取的数据添加到列表中
        dataframes.append(df)
merged_df = pd.concat(dataframes, ignore_index=True)
merged_df.to_csv(output_path, index=False)
print(f"所有CSV文件已合并并导出到 {output_path}")

