


# 下载地址页面
# https://fis.fda.gov/extensions/FPD-QDE-FAERS/FPD-QDE-FAERS.html


# 下载地址示例
# https://fis.fda.gov/content/Exports/faers_ascii_2012q4.zip


# 2012只有一个
print('https://fis.fda.gov/content/Exports/faers_ascii_2012q4.zip')


# 2013-2018 路径是小q
for i in range(2013, 2018 + 1):
    for j in range(1, 4 + 1):
        print(f'https://fis.fda.gov/content/Exports/faers_ascii_{i}q{j}.zip')
    
# 2019-2023 路径是大Q
for i in range(2019, 2023 + 1):
    for j in range(1, 4 + 1):
        print(f'https://fis.fda.gov/content/Exports/faers_ascii_{i}Q{j}.zip')
        
