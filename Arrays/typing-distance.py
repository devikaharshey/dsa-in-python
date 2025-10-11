# Typing Distance - Hackerrank
def getDistance(word):
    keyboard = [
    ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0'],
    ['Q', 'W', 'E', 'R', 'T', 'Y', 'U', 'I', 'O', 'P'],
    ['A', 'S', 'D', 'F', 'G', '*', 'H', 'J', 'K', 'L'],
    ['', 'Z', 'X', 'C', 'V', 'B', 'N', 'M', '', '']
    ]
    
    def getIndex(ch):
        n = len(keyboard)
        m = len(keyboard[0])
        
        for i in range(n):
            for j in range(m):
                if keyboard[i][j] == ch:
                    return [i, j]
        return [0, 0]
    
    totalDistance = 0
    prev = getIndex('*') 
    
    for ch in word:
        curr = getIndex(ch)
        totalDistance += abs(prev[0]-curr[0]) + abs(prev[1]-curr[1])
        prev = curr
            
    return totalDistance
    
print(getDistance("QZ"))
print(getDistance("MNYV"))
print(getDistance("DEVIKA"))
print(getDistance("HARSHEY"))