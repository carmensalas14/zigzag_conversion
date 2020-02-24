'''
pedac
- for numOfRows , create num of rows list to hold chars 
- create a varibale that was direction of zig zag pattern/incrementation 
- create counter 'count' that controls iteration over lists 
- if isDown count += 1
- array with num arrays of row num 
- array rows = []

'''

def zig_zag(string,numRows):
    rows = []
    for i in range(numRows):
        rows.append([])
    count = 0
    output = ''
     
    for letter in string:
        if count == 0:
            isDown = True
        elif count == numRows - 1:
            isDown = False
        
        rows[count].append(letter)
        if isDown:
            count += 1
        else:
            count -= 1
    print(rows)
    for row in rows:
        output += "".join(row)
    return output
        
print(zig_zag('stephsmith', 3))
        
    