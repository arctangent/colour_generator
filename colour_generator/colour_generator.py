
from random import uniform
from tkinter import *
from PIL import ImageGrab

from colour_generator_classes import Colour, ColourGenerator


# INSTRUCTIONS
# - Press "m" to cycle through modes
# - Press "s" to save an image
# - Press any other key to generate new colours in same mode
# - Click mouse to see colour values

canvas_width = 800
canvas_height = 800

# Set up GUI
window = Tk()
window.resizable(False, False)
canvas = Canvas(window, width=canvas_width, height=canvas_height, bd=0, highlightthickness=0)
canvas.pack()

MODE = "STANDARD"
counter = 0
    
    
def draw_box(x1, y1, x2, y2, h, s, b):
    '''
    Utility function to draw a colour and its shades
    '''
 
    # Represent the colour using our custom Colour class
    # so that we can easily calculate shades 
    c = Colour(h, s, b)
 
    # Some math for the main box
    box_width = x2 - x1
    box_height = y2 - y1
    
    # Some math for shades
    shade_width = box_width / c.num_shades
    shade_height = box_height / 3
    shade_y2 = y1 + shade_height
    
    # Draw main box
    fill = c.as_rgb_string()
    canvas.create_rectangle(x1, y1, x2, y2, fill=fill, width=0)

    # Draw shades
    for i in range(c.num_shades):
        shade = c.shades()[i]
        fill = shade.as_rgb_string()
        canvas.create_rectangle(x1 + i * shade_width, y1, x1 + (i+1) * shade_width, shade_y2, fill=fill, width=0)

    
def draw():
    '''
    Generate and draw some colours
    '''
    
    # We use this counter to name any images we save
    global counter
    counter += 1
    
    # These are fairly decent default values
    s = 80
    b = 50
    
    if MODE == 'STANDARD':
        '''
        Generates and draws a primary colour, its complement, and two adjacent colours
        '''
        
        # Set adjacency amount to use
        adjacency = 30 + uniform(0, 90)
    
        # Generate primary hue
        h = uniform(0, 360)
        
        # Draw primary colour box in top half of screen
        draw_box(0, 0, canvas_width, canvas_height/2, h, s, b)
        
        # Draw complementary colour box below at half height
        h_complement = ColourGenerator.get_complementary_hue(h)
        draw_box(0, canvas_height/2, canvas_width, 0.75 * canvas_height, h_complement, s, b)
        
        # Draw adjacent colour boxes in very bottom left and very bottom right
        h_left, h_right = ColourGenerator.get_adjacent_hues(h, adjacency)
        draw_box(0, 0.75*canvas_height, canvas_width/2, canvas_height, h_left, s, b)
        draw_box(canvas_width/2, 0.75*canvas_height, canvas_width, canvas_height, h_right, s, b)
        
    elif MODE == 'TRIAD':
        '''
        Generates and draws three colours equidistant on colour wheel
        '''
        
        # Generate the three hues
        h1, h2, h3 = ColourGenerator.generate_triad_hues()
        
        # Draw first hue in top half of screen
        draw_box(0, 0, canvas_width, canvas_height/2, h1, s, b)
        
        # Draw the other two hues in bottom left and bottom right
        draw_box(0, canvas_height/2, canvas_width/2, canvas_height, h2, s, b)
        draw_box(canvas_width/2, canvas_height/2, canvas_width, canvas_height, h3, s, b)
        
    elif MODE == 'TETRAD':
        '''
        Generates and draws four colours equidistant on colour wheel
        '''
        
        # Generate the four hues
        h1, h2, h3, h4 = ColourGenerator.generate_tetrad_hues()
        
        # Draw each one in a corner of the screen
        draw_box(0, 0, canvas_width/2, canvas_height/2, h1, s, b)
        draw_box(canvas_width/2, 0, canvas_width, canvas_height/2, h2, s, b)
        draw_box(0, canvas_height/2, canvas_width/2, canvas_height, h3, s, b)
        draw_box(canvas_width/2, canvas_height/2, canvas_width, canvas_height, h4, s, b)

    # Update canvas
    canvas.update()
        

# --------------------------------------------------------------   
# INTERACTIVITY
    
def save_image(*ignore):
    '''
    Allow user to save an image
    '''

    # The name of our image
    image_name = 'images/' + str(counter).zfill(8) + '.png'

    # Compute location of screen to grab
    x1 = window.winfo_rootx() + canvas.winfo_x()
    y1 = window.winfo_rooty() + canvas.winfo_y()
    x2 = x1 + canvas.winfo_width()
    y2 = y1 + canvas.winfo_height()
    
    # Save the image
    ImageGrab.grab((x1, y1, canvas_width, canvas_height)).save(image_name)



def change_mode(*ignore):
    '''
    Allow user to cycle between modes
    '''
    
    global MODE
    modes = ['STANDARD', 'TRIAD', 'TETRAD']
    current_mode_position = modes.index(MODE)
    next_mode_position = (current_mode_position + 1) % len(modes)
    MODE = modes[next_mode_position]
        
    # Redraw the screen on any keypress
    draw()


# Bind keys
window.bind('m', change_mode)
window.bind('s', save_image)


# --------------------------------------------------------------   
# EXECUTE
 
draw()
window.mainloop()
