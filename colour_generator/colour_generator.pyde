from __future__ import division 

from colour_generator_classes import Colour, ColourGenerator


# INSTRUCTIONS
# - Press "m" to cycle through modes
# - Press "s" to save an image
# - Press any other key to generate new colours in same mode
# - Click mouse to see colour values


def setup():
    '''
    Initial setup
    '''
    
    # Set screen size
    size(800, 800)
    
    # Disable animation
    noLoop() 
    
    # Disable outlines around rectangles
    noStroke()

    # Set colour mode
    colorMode(HSB, 360, 100, 100)
    
    # Set global variable allowing cycling between generation method
    global MODE
    MODE = "STANDARD" 
    
    
def draw_box(x1, y1, x2, y2, h, s, b):
    '''
    Utility function to draw a colour and its shades
    '''
 
    # Represent the colour using our custom Colour class
    # so that we can easily calculate shades 
    c = Colour(h, s, b)
 
    # Some math for the main box
    rectMode(CORNERS)
    box_width = x2 - x1
    box_height = y2 - y1
    
    # Some math for shades
    shade_width = box_width / c.num_shades
    shade_height = box_height / 3
    shade_y2 = y1 + shade_height
    
    # Draw main box
    fill(h, s, b)
    rect(x1, y1, x2, y2)
    
    # Draw shades
    for i in xrange(c.num_shades):
        shade = c.shades()[i]
        fill(shade.h, shade.s, shade.b)
        rect(x1 + i * shade_width, y1, x1 + (i+1) * shade_width, shade_y2)

    
def draw():
    '''
    Generate and draw some colours
    '''
    
    # These are fairly decent default values
    s = 50
    b = 50
    
    if MODE == 'STANDARD':
        '''
        Generates and draws a primary colour, its complement, and two adjacent colours
        '''
        
        # Set adjacency amount to use
        adjacency = 30 + random(90)
    
        # Generate primary hue
        h = random(360)
        
        # Draw primary colour box in top half of screen
        draw_box(0, 0, width, height/2, h, s, b)
        
        # Draw complementary colour box below at half height
        h_complement = ColourGenerator.get_complementary_hue(h)
        draw_box(0, height/2, width, 0.75 * height, h_complement, s, b)
        
        # Draw adjacent colour boxes in very bottom left and very bottom right
        h_left, h_right = ColourGenerator.get_adjacent_hues(h, adjacency)
        draw_box(0, 0.75*height, width/2, height, h_left, s, b)
        draw_box(width/2, 0.75*height, width, height, h_right, s, b)
        
    elif MODE == 'TRIAD':
        '''
        Generates and draws three colours equidistant on colour wheel
        '''
        
        # Generate the three hues
        h1, h2, h3 = ColourGenerator.generate_triad_hues()
        
        # Draw first hue in top half of screen
        draw_box(0, 0, width, height/2, h1, s, b)
        
        # Draw the other two hues in bottom left and bottom right
        draw_box(0, height/2, width/2, height, h2, s, b)
        draw_box(width/2, height/2, width, height, h3, s, b)
        
    elif MODE == 'TETRAD':
        '''
        Generates and draws four colours equidistant on colour wheel
        '''
        
        # Generate the four hues
        h1, h2, h3, h4 = ColourGenerator.generate_tetrad_hues()
        
        # Draw each one in a corner of the screen
        draw_box(0, 0, width/2, height/2, h1, s, b)
        draw_box(width/2, 0, width, height/2, h2, s, b)
        draw_box(0, height/2, width/2, height, h3, s, b)
        draw_box(width/2, height/2, width, height, h4, s, b)
        

# --------------------------------------------------------------   
# INTERACTIVITY
    
    
def keyPressed():
    '''
    Handle keyboard events
    '''
    
    # Allow change of modes
    if key == 'm':
        global MODE
        modes = ['STANDARD', 'TRIAD', 'TETRAD']
        current_mode_position = modes.index(MODE)
        next_mode_position = (current_mode_position + 1) % len(modes)
        MODE = modes[next_mode_position]
        print "MODE: %s" % MODE
        
    # Allow saving of images
    elif key == 's':
        saveFrame("images/%s-####.png" % MODE)
    
    # Redraw the screen on any keypress
    redraw()

                
def mouseClicked():
    '''
    Handle mouse click event
    '''

    # Load information about the pixel that was clicked
    loadPixels()
    c = pixels[mouseY*width + mouseX]
    
    # Tell the user what the colour value is for that pixel
    print "---"
    print "HSB: %s, %s, %s" % (hue(c), saturation(c), brightness(c))
    print "RGB: %s, %s, %s" % (red(c), green(c), blue(c))
    
    
    