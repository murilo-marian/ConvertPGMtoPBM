def readImage(filepath):
    with open(filepath, "r") as image:
        imageType = image.readline().strip()
        assert imageType == "P2", "Não é P2"
        
        line = image.readline().strip()
        
        width, height = map(int, line.split())
        grayscaleBits = int(image.readline().strip())
        
        pixels = []
        for _ in range(height):
            row = []
            for _ in range(width):
                row.append(image.readline().strip())
            pixels.append(row)
        
    return pixels, grayscaleBits, width, height

def convertBits(pixels, limiar, width, height):
    convertedPixelsFixed = []
    convertedPixelsDynamic = []
    for y in range(height):
        fixedRow = []
        dynamicRow = []
        for x in range(width):
            chosenPixel = pixels[y][x]
            fixed = 1
            if int(chosenPixel) <= 128:
                fixed = 0
                print("ttestse")
                
            dynamic = 1
            if int(chosenPixel) <= limiar:
                dynamic = 0
            fixedRow.append(fixed)
            dynamicRow.append(dynamic)
        convertedPixelsFixed.append(fixedRow)
        convertedPixelsDynamic.append(dynamicRow)
    
    return convertedPixelsFixed, convertedPixelsDynamic


def saveIMG(filename, pixels, width, height):
    with open(filename, "w") as newImage:
        newImage.write("P1\n")
        newImage.write(str(width) + " " + str(height) + "\n")
        
        for row in pixels:
            newImage.write(" ".join(map(str, row)) + "\n")
            

def saveIMGNegative(filename, pixels, width, height):
    with open(filename, "w") as newImage:
        newImage.write("P1\n")
        newImage.write(str(width) + " " + str(height) + "\n")
        
        for row in pixels:
            newImage.write(" ".join(map(lambda x: '0' if x == 1 else '1', row)) + "\n")
            
            
originalIMG = "Entrada_EscalaCinza.pgm"

pixels, bits, width, height = readImage(originalIMG)
limiar = 40
convertedPixelsFixed, convertedPixelsDynamic = convertBits(pixels, limiar, width, height)

output = "BlackWhite.pbm"

saveIMGNegative("negative" + output, convertedPixelsFixed, width, height)
saveIMG(output, convertedPixelsFixed, width, height)
saveIMG("dynamic" + output, convertedPixelsDynamic, width, height)