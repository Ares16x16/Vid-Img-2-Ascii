# Vid-Img-2-Ascii
## Screen Capture to ASCII Art in Terminal
This is a Python program that captures your screen and converts it to ASCII art in terminal. The program uses the PyAutoGUI module to capture a screenshot of the screen, and then uses OpenCV to convert the image to grayscale and resize it to fit the terminal window. Finally, the program converts the grayscale image to ASCII art by mapping the pixel values to ASCII characters.

### Usage
To use the program, simply run the ScreenCapture class:
```python
if __name__ == "__main__":
    screen_capture = ScreenCapture()
    screen_capture.start_capture()
```
By default, the program uses the ASCII_CHARS list to map the pixel values to ASCII characters. You can also use a different set of ASCII characters by creating a new list and passing it to the ASCII_CHARS variable:
```python
ASCII_CHARS = "@WM%#&$~^[]`\')(|\\/:+=-,.            "
```
You can then call the start_capture method to begin capturing the screen and converting it to ASCII art.
You can exit the program by pressing ```Ctrl + C``` in the terminal.
## Image to ASCII Converter
This is a simple Python program that converts an image to ASCII art and stores it in txt file. The program uses the Python Imaging Library (PIL) to open and manipulate the image, and then converts the image to ASCII art by mapping the pixel values to ASCII characters.

### Usage
To use the program, simply run the ImageToAsciiConverter class with the path to the input image as an argument:
```python
img = 'input_image.jpg'
converter = ImageToAsciiConverter(img)
```

You can then convert the image to ASCII art by calling the convert_image_to_ascii method:
```python
converter.convert_image_to_ascii()
```
By default, the program will use the ASCII_CHARS list to map the pixel values to ASCII characters. You can also use a different set of ASCII characters by creating a new list and passing it to the ASCII_CHARS variable:
```python
ASCII_CHARS = "$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,\"^`'.         "
```
You can then call the convert_image_to_ascii method again to generate the ASCII art with the new character set.

You can save the ASCII art to a file by calling the save_ascii_image method:
```python
converter.save_ascii_image('output_file.txt')
```

And you can print the ASCII art to the console by calling the print_ascii_image method:
```python
converter.print_ascii_image()
```
