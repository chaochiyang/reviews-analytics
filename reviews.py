data = []                             # 設定一個叫做data的空清單  
count = 0 
with open ('reviews.txt', 'r') as f:  # 將.txt黨打開，讀取成為 f
	for line in f:                    # 將 f 中一筆一筆取出來成為 line  
		data.append(line)             # append line 加到 data 清單中  
		count += 1                    # count = count +1
		if count % 100000 == 0: 	  # % 是 除以___的餘數
			print(len(data))          # 印出data的長度(幾筆reviews) 
	
print('檔案讀取完了，總共有', len(data), '筆資料')


sum_len = 0
for d in data:     # 把 data 清單中的每筆留言一筆筆取出來成為 d （每筆留言是一個d） 
	sum_len = sum_len + len(d)      # 所有留言的長度總和（迴圈依照順序加總到最後一筆）

print('平均留言長度為', sum_len/len(data))


new = [] 
for d in data:
	if len(d) < 100:
		new.append(d) 
print('一共有', len(new), '筆留言長度小於100')
print(new[0])
print(new[1])