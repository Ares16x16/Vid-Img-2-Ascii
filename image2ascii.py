from PIL import Image

ASCII_CHARS = "@WM%#&$~^[]`\')(|\\/:+=-,.     "
ASCII_CHARS1 = "$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,\"^`'.         " # From geeksforgeeks

class ImageToAsciiConverter:
    def __init__(self, image_path):
        self.image_path = image_path
        self.ascii_image = ''

    def convert_image_to_ascii(self,asciiPart='img'): # asciiPart='img'/'bg'
        image = Image.open(self.image_path)
        image = image.resize((80, 40))
        image = image.convert('L')
        
        if asciiPart == 'bg':
            image = image.point(lambda pixel: 255 - pixel)
        """elif asciiPart == 'img':
            pass"""
            
        pixels = list(image.getdata())

        for i in range(0, len(pixels), image.width):
            ascii_row = ''
            for pixel_value in pixels[i:i+image.width]:
                ascii_index = ascii_index = pixel_value * (len(ASCII_CHARS)-1) // 255  # Mapping
                ascii_row += ASCII_CHARS[ascii_index]
            self.ascii_image += ascii_row + '\n'
            
    def save_ascii_image(self, output_path):
        with open(output_path, 'w') as file:
            file.write(self.ascii_image)
            
    def print_ascii_image(self):
        print(self.ascii_image)       

if __name__ == '__main__':
    img = 'shibuyakanon.jpg'
    converter = ImageToAsciiConverter(img)
    converter.convert_image_to_ascii('bg')
    converter.save_ascii_image('kanon.txt')
    converter.print_ascii_image()