from PIL import Image

letterHeight = 150
letterWidth = 150
charsInLine = 7

def load_image(file_path):
    try:  
        img = Image.open(file_path)
        return img
    except IOError:
        print("Error in extraction. File " + file_path + " ot found")
        
def formatToLetterList(userStr):
    rows = []
    
    asLetterList = [char for char in userStr]

    while len(asLetterList) > 0:
        arr = []
        for i in range(charsInLine):
            if len(asLetterList) > 0:      
                arr.append(asLetterList[0])
                del asLetterList[0]
        rows.append(arr)

    print(rows)
    return rows

def formatToLinkList(rows):
    for row in range(len(rows)):
        for i in range(len(rows[row])):
            char = rows[row][i]

            if char == 'A':
                rows[row][i] = "letters/upperA.png"
            elif char == 'a':
                rows[row][i] = "letters/lowerA.png"
            else:
                rows[row][i] = "test.png"

    print(rows)
    return rows
    
def main():
    base = load_image("base.png")

    userInput = input("Please input a string")

    formatted = formatToLinkList(formatToLetterList(userInput))

    for row in range(len(formatted)):
        for i in range(len(formatted[row])):
            base.paste(Image.open(formatted[row][i]), ((i*letterWidth), (row*letterHeight)))

    base.save('result.png', quality = 100)

    file_in = "result.png"
    img = Image.open(file_in)

    file_out = "result.bmp"
    img.save(file_out)

main()
