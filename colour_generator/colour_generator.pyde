

'''
Generates:
    - A primary hue
    - Its complement
    - And two adjacent colours
'''

from __future__ import division



# TODO: Extract the logic of this out into a Class

# NUM_SHADES must be > 1
NUM_SHADES = 4

ADJACENCY_AMOUNT = 30

SHADE_SATURATION_MIN = 30
SHADE_SATURATION_MAX = 70
SHADE_BRIGHTNESS_MIN = 70
SHADE_BRIGHTNESS_MAX = 30


def setup():
    size(800, 800)
    noLoop() 
    noStroke()
    colorMode(HSB, 360, 100, 100)
    
    
def draw_box(x1, y1, x2, y2, h, s, b):
 
    rectMode(CORNERS)
    box_width = x2 - x1
    box_height = y2 - y1
    
    # Draw main box
    fill(h, s, b)
    rect(x1, y1, x2, y2)
    
    # Draw shades
    
    shade_width = box_width / NUM_SHADES
    shade_height = box_height / 3
    shade_y2 = y1 + shade_height
    
    for i in range(NUM_SHADES):
        s_val = SHADE_SATURATION_MIN + i * (SHADE_SATURATION_MAX - SHADE_SATURATION_MIN) / (NUM_SHADES - 1)
        b_val = SHADE_BRIGHTNESS_MIN + i * (SHADE_BRIGHTNESS_MAX - SHADE_BRIGHTNESS_MIN) / (NUM_SHADES - 1)
        fill(h, s_val, b_val)
        rect(x1 + i * shade_width, y1, x1 + (i+1) * shade_width, shade_y2)

    
def draw():
    
    # Generate primary colour
    h = random(360)
    s = (SHADE_SATURATION_MIN + SHADE_SATURATION_MAX) / 2
    b = (SHADE_BRIGHTNESS_MIN + SHADE_BRIGHTNESS_MAX) / 2
    
    # Draw primary colour box
    draw_box(0, 0, width, height/2, h, s, b)
    
    # Draw complementary colour box
    h_complement = (h + 180) % 360
    draw_box(0, height/2, width, 0.75 * height, h_complement, s, b)
    
    # Draw adjacent colour boxes
    h_left = (h - ADJACENCY_AMOUNT) % 360
    h_right = (h + ADJACENCY_AMOUNT) % 360
    draw_box(0, 0.75*height, width/2, height, h_left, s, b)
    draw_box(width/2, 0.75*height, width, height, h_right, s, b)
    
    
    
    
def keyPressed():
    redraw()

        
def mouseClicked():
    loadPixels()
    c = pixels[mouseY*width + mouseX]
    print "---"
    print "HSB: %s, %s, %s" % (hue(c), saturation(c), brightness(c))
    print "RGB: %s, %s, %s" % (red(c), green(c), blue(c))
    
    
    
