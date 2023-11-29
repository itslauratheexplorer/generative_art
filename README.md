# Generative Artwork
This Python script enables to creates generative art images by combining random shapes, a images, and text on a colorful background. Right now the script is modifiied to create colorful rectangles, a star image and song quotes on randomly changing colorful backgrounds.
The python file is called "generative_gracie_artwork" since the used quotes and image are references to singer Gracie Abrams. There for my code and the generated art works are based on her and her music. 
(But the code is editable as desired)

# Prerequisites
- Python 3.9.7 (Version I used and can asure it works on)
- Pillow library
Install Pillow librabry in your terminal 
```bash
pip install pillow
```
# Assets 
Download "Gracie_star_white.png" and the "HannaHandwriting.ttf" font from the assets folder. 

Replace the place holder path in the script with your image and font path:
```bash
star_image = Image.open('/path/to/Gracie_star_white.png')
```
```bash
font_path = "/path/to/HannaHandwriting.ttf"
```

# Configuration and Customization
- Background Colors: Modify the background_colors list to set the available background colors.
- Quotes: Update the quotes list with your desired quotes or any text.
- Fonts: Change the font_path variable to the path of your preferred font.
- Images: Change the image by replacing the star_image path for your own imgage. I recommend using an image with transparent background.
- Shapes: adjust the color, shape and number of shapes within the def darw_random_shape function.

Detailed description of the code and each function is documented in the python script

# Run the script 
After either cloning the repository:
```bash
   git clone https://github.com/itslauratheexplorer/generative_art.git
```
Or copying the script and downloading the assets run the script:
```bash
python generative_gracie_artwork.py
```

# Acknowledgement 
- Source Code for generating random shapes by: HAMY LABS
  (https://www.youtube.com/watch?v=pDnjLqExT4s&list=PLGbSZMk99rOTjJ0N140Dz1Vd7o8WLhjNi&index=2&t=503s)
- Quotes inspired by Gracie Abrams 
