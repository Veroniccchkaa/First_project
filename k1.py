text = 'uhjjjfjfgfgfj gfjhgffdr658rre475 uhgj xyeye v, ., y i65545ritjyg klj..nyt. 7 yg'
char_count = {}

for char in text:
    if char in char_count:
        char_count[char] += 1
    else: 
        char_count[char] = 1
        
print(char_count)