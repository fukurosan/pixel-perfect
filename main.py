import sys
import argparse
from pathlib import Path
import random
from PIL import Image


def main():
    if isFile(INPUT_FILE):
        
        if OPERATION == "encrypt":
            img = Image.open(INPUT_FILE)
            pixels = encryptPixels(img)
            saveImage(INPUT_FILE + "_encrypted.png", img.size, pixels)
        
        elif OPERATION == "decrypt":
            img = Image.open(INPUT_FILE)
            pixels = decryptPixels(img)
            saveImage(INPUT_FILE + "_decrypted.png", img.size, pixels)
        
        else:
            sys.exit("Supported operations are encrypt or decrypt: " + OPERATION)

    else:
        print("No such file found!")


def isFile(fileLocation):
    imagePath = Path(fileLocation)
    return imagePath.is_file()


def getPixels(img):
    width, height = img.size
    pixels = []
    for x in range(width):
        for y in range(height):
            pixels.append(img.getpixel((x, y)))
    return pixels


def shuffleIndex(pixels):
    index = list(range(len(pixels)))
    random.shuffle(index)
    return index


def encryptPixels(img):
    random.seed(hash(img.size))
    pixels = getPixels(img)
    index = shuffleIndex(pixels)
    newPixelMap = []
    for i in index:
        newPixelMap.append(pixels[i])
    return newPixelMap


def decryptPixels(img):
    random.seed(hash(img.size))
    pixels = getPixels(img)
    index = shuffleIndex(pixels)
    newPixelMap = list(range(len(pixels)))
    current = 0
    for i in index:
        newPixelMap[i] = pixels[current]
        current += 1
    return newPixelMap


def saveImage(name, size, pixels):
    image = Image.new("RGB", size)
    width, height = size
    pixelIterator = iter(pixels)
    for x in range(width):
        for y in range(height):
            image.putpixel((x, y), pixelIterator.__next__())
    image.save(name)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='encrypts and decrypts images by shuffling its pixels.')
    parser.add_argument('--file', type=str, help="The file to be handled.")
    parser.add_argument('--operation', type=str, help="Encrypt or Decrypt.")
    args = parser.parse_args()
    
    INPUT_FILE = args.file
    OPERATION = args.operation

    assert INPUT_FILE != None, "You need to specify a file. Use --file"
    assert OPERATION != None, "You need to specify an operation. Use --operation"

    main()
