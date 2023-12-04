#inital setup 
import os #provides interaction with operating system
import random 
import uuid #generates unique IDs 
from PIL import Image, ImageDraw, ImageFont #Python Imaging Library with classes for image and font processing

#generates a unique ID for each run
run_id = uuid.uuid1()

#checks for output directory; creates one of not existing (will hold files)
output_directory = "./output"
if not os.path.exists(output_directory):
    os.makedirs(output_directory)

#prints out generated ID for each run 
print(f"Processing run_id:{run_id}")

#list of background colors (RGB)
background_colors = [(0, 47, 201), (211, 64, 221), (66, 66, 66), (242, 161, 0), (123, 0, 255)]

#list of song quotes
song_quotes = ["I miss you, I'm sorry.", "I see you every night in my sleep.", "Now I'm half of myself here without you.",
          "I still love you, I promise.", "You're a bad holiday.", "You're the worst of my crimes.", 
          "I held myself because you wouldn't.","I'm gonna drag you right down to the bottom.",
          "I'm sure that I would like her,\nif I were slightly nice.", "You said forever and I almost bought it.",
          "Could you hold me\nwithout any talking?"]

#chooses random background color and quote out of each list 
background_color = random.choice(background_colors)
song_quotes = random.choice(song_quotes)

#creates main RGB image/ canvas used as background
image = Image.new("RGB", (2000, 2000), background_color)
width, height = image.size

#creates object for drawing on the main image 
draw_image = ImageDraw.Draw(image)

#function draws random shapes, is currently set to drawing rectangles 
def draw_random_shape(draw, x, y, size):
    shape_rect = [
        (x - size / 2, y - size / 2),
        (x + size / 2, y + size / 2)
    ]
    #sets randomly color for the shape within specified RGB values 
    shape_color = (
        random.randint(0, 240),
        random.randint(0, 240),
        random.randint(0, 240)
    )
    draw.rectangle(shape_rect, fill=shape_color)

#defines the desired number of shapes
number_of_shapes = 3 

#calls number of shapes; randomly determines sizes of the shapes within bounds
for _ in range(number_of_shapes):
    shape_x = random.randint(0, width)
    shape_y = random.randint(0, height)
    shape_size = random.randint(800, 1500)

    draw_random_shape(draw_image, shape_x, shape_y, shape_size)

#function pastes image, in this case star image, onto the main canvas
#position and size are randomized within a certain range 
def draw_star(draw, min_size, max_size):
    star_size = random.randint(min_size, max_size)
    star_image = Image.open('/path/to/Gracie_star_white.png') #replace with your own path
    #ANTIALIAS smoothes edges of image when being resized
    star_image = star_image.resize((star_size, star_size), Image.ANTIALIAS) 
    x = random.randint(0, width)
    y = random.randint(0, height)
    #coordinates are used to determine (random) placemtn of the star image 
    image.paste(star_image, (x - star_size // 2, y - star_size // 2), star_image)

#defines minimum and maximum size of the star image; generated randomly within this range
min_star_size = 200
max_star_size = 1200
#calls function --> draws star image 
draw_star(draw_image, min_star_size, max_star_size)

#defines text color (RGB code), text size and font 
quote_color = (255, 255, 255)
font_size = 65
font_path = "/path/to/HannaHandwriting.ttf"  #replace with your own path
font = ImageFont.truetype(font_path, font_size)

#positions text randomly within a specified range (to prevent text from being cut off) 
text_x = random.randint(500, width - 1400)
text_y = random.randint(200, height - 200)

#draws text (song quotes) on the image
draw_image.text((text_x, text_y), song_quotes, font=font, fill=quote_color)

#saves image in output directory; creates unique filename 
image.save(f"{output_directory}/{run_id}.png")
