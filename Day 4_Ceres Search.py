#--- Day 4: Ceres Search ---
# Here i m gonna use the daa a 2D array , i build it like a grid and defining directions to use it 
# where each letter is at a position (row, col).

def xmas_counting(grid):
    word = "XMAS"
    rows = len(grid)
    cols = len(grid[0])
    somme_xmas = 0
    directions = [
        (0, 1),   
        (0, -1),  
        (1, 0),   
        (-1, 0),  
        (1, 1),   
        (1, -1),  
        (-1, -1), 
        (-1, 1),  
    ]

    for i in range(rows):
        for j in range(cols):
            for dr, dc in directions:
                letters = []
                for k in range(len(word)):
                    n_i = i + dr * k
                    n_j = j + dc * k
                    if 0 <= n_i < rows and 0 <= n_j < cols:
                        letters.append(grid[n_i][n_j])
                    else:
                        break
                if ''.join(letters) == word:
                    somme_xmas= somme_xmas+ 1

    return somme_xmas
    
#Lets try it on the example
example = [
    "MMMSXXMASM",
    "MSAMXMSMSA",
    "AMXSXMAAMM",
    "MSAMASMSMX",
    "XMASAMXAMM",
    "XXAMMXXAMA",
    "SMSMSASXSS",
    "SAXAMASAAA",
    "MAMMMXMMMM",
    "MXMXAXMASX"
]
print("Times  XMAS appear = ", xmas_counting(example))

# now on the puzzle input 
with open("C:/Users/21629/Desktop/code/day4_data.txt", "r") as file:
    grid = [line.strip() for line in file if line.strip()]


print("Times  XMAS appear = ", xmas_counting(grid))
#Times  XMAS appear =2358


#--- Part Two ---

def x_mas_counting(grid):
    rows = len(grid)
    cols = len(grid[0])
    somme_x_mas = 0
    def is_mas(triplet):
        return triplet == ['M', 'A', 'S'] or triplet == ['S', 'A', 'M']

    for i in range(1, rows - 1):
        for j in range(1, cols - 1):
            if grid[i][j] != 'A':
                continue  
            diag_1 = [grid[i - 1][j - 1], grid[i][j], grid[i + 1][j + 1]]
            diag_2 = [grid[i - 1][j + 1], grid[i][j], grid[i + 1][j - 1]]

            if is_mas(diag_1) and is_mas(diag_2):
                somme_x_mas =somme_x_mas+ 1

    return somme_x_mas

example2 = [
    ".M.S......",
    "..A..MSMS.",
    ".M.S.MAA..",
    "..A.ASMSM.",
    ".M.S.M....",
    "..........",
    "S.S.S.S.S.",
    ".A.A.A.A..",
    "M.M.M.M.M.",
    ".........."
]
print('Times does an X-MAS appear =',x_mas_counting(example2))
with open("C:/Users/21629/Desktop/code/day4_data.txt", "r") as file:
    grid = [line.strip() for line in file if line.strip()]


print('Times does an X-MAS appear =', x_mas_counting(grid))
#Times does an X-MAS appear = 1737