sudoku = [
    [8,0,0,9,3,0,0,0,2],
    [0,0,9,0,0,0,0,4,0],
    [7,0,2,1,0,0,9,6,0],
    [2,0,0,0,0,0,0,9,0],
    [0,6,0,0,0,0,0,7,0],
    [0,7,0,0,0,6,0,0,5],
    [0,2,7,0,0,8,4,0,6],
    [0,3,0,0,0,0,5,0,0],
    [5,0,0,0,6,2,0,0,8]
]

def tablo(s):
    for i in range(len(s)):
        if i % 3 == 0:
            print()
        for j in range(len(s[0])):
            if j % 3 == 0:
                print(end="")
            elif j == 8:
                print(s[i][j])
            else:
                print(s[i][j], end="")

def uygun(satir, sutun, sayi):
    global sudoku
    if sayi in sudoku[satir]:
        return False
    for i in range(len(sudoku[0])):
        if sudoku[i][sutun] == sayi:
            return False
    r = (satir // 3) * 3
    c = (sutun // 3) * 3
    for i in range(r, r+3):
        for j in range(c, c+3):
            if sudoku[i][j] == sayi:
                return False
    return True

def cozum():
    global sudoku
    for satir in range(len(sudoku[0])):
        for sutun in range(len(sudoku)):
            if sudoku[satir][sutun] == 0:
                for sayi in range(1, 10):
                    if uygun(satir, sutun, sayi):
                        sudoku[satir][sutun] = sayi
                        cozum()
                        sudoku[satir][sutun] = 0
                return
    tablo(sudoku)

cozum()

