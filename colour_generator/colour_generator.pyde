from __future__ import division 

from abc import ABCMeta, abstractmethod


class ColourGenerator(object):
    '''
    A class to help with colour generation
    
    Assumes colorMode(HSB, 360, 100, 100)
    '''
    
    # This is an abstract class
    # i.e. it cannot be instantiated
    __metaclass__ = ABCMeta
    
    #
    # Generate sets of colours
    #
    
    @staticmethod
    def generate_complementary_hues(hue_val=None):
        # Returns two complementary hues
        h1 = hue_val or random(360)
        h2 = (hue_val + 180) % 360
        
    @staticmethod
    def generate_triad_hue(hue_val=None):
        # Returns three hues equidistant on colour wheel
        h1 = hue_val or random(360)
        h2 = (hue_val + 120) % 360
        h3 = (hue_val - 120) % 360
        return h1, h2, h3
    
    @staticmethod
    def generate_tetrad_hue(hue_val=None):
        # Returns four hues equidistant on colour wheel
        h1 = hue_val or random(360)
        h2 = (hue_val + 90) % 360
        h3 = (hue_val + 180) % 360
        h4 = (hue_val + 270) % 360
        return h1, h2, h3, h4
    
    #
    # Other useful class methods
    #
        
    @staticmethod
    def generate_random_hsb(h=None, s=None, b=None):
        # Return a random colour, allowing user to specify fixed values if required
        h = h or random(360)
        s = s or random(100)
        b = b or random(100)
        return h, s, b
        
        
    @staticmethod
    def get_complementary_hue(hue_val):
        # Return the hue on the opposite side of the colour wheel
        complement = (hue_val + 180) % 360
        return complement
    
    @staticmethod
    def get_adjacent_hues(hue_val, degree_distance):
        # Return the two colours obtained by travelling the
        # colour wheel degree_distance each side
        h_left = (hue_val - degree_distance) % 360
        h_right = (hue_val + degree_distance) % 360
        return h_left, h_right
    

class Colour(object):
    '''
    A class to help manipulate a particular colour
    
    Assumes colorMode(HSB, 360, 100, 100)
    '''
    
    def __init__(self, h=None, s=None, b=None):
        # Hue, Saturation, Brightness
        self.h, self.s, self.b = h, s, b
        # Each colour can contain a swatch of shades,
        # each of which is also a Colour
        self._shades = []
        self.num_shades = 4
        self.shade_saturation_min = 30
        self.shade_saturation_max = 70
        self.shade_brightness_min = 70
        self.shade_brightness_max = 30
        
    def shades(self):
        '''
        Return a list of shades
        '''
    
        if self._shades:
            return self._shades
        
        # Generate shades
        shades = []
        for i in range(self.num_shades):
            s_val = self.shade_saturation_min + i * (self.shade_saturation_max - self.shade_saturation_min) / (self.num_shades - 1)
            b_val = self.shade_brightness_min + i * (self.shade_brightness_max - self.shade_brightness_min) / (self.num_shades - 1)
            shade = Colour(self.h, s_val, b_val)
            shades.append(shade)
            
        # Memoise and return
        self._shades = shades
        return shades





'''
Generates:
    - A primary hue
    - Its complement
    - And two adjacent colours
    
    
TODO:
    - Add drawing modes for Triad and Tetrad
    - Allow user to cycle between them
'''



def setup():
    size(800, 800)
    noLoop() 
    noStroke()
    colorMode(HSB, 360, 100, 100)
    
    
def draw_box(x1, y1, x2, y2, h, s, b):
 
    c = Colour(h, s, b)
 
    rectMode(CORNERS)
    box_width = x2 - x1
    box_height = y2 - y1
    
    # Draw main box
    fill(h, s, b)
    rect(x1, y1, x2, y2)
    
    # Draw shades
    
    shade_width = box_width / c.num_shades
    shade_height = box_height / 3
    shade_y2 = y1 + shade_height
    

    
    for i in xrange(c.num_shades):
        shade = c.shades()[i]
        fill(shade.h, shade.s, shade.b)
        rect(x1 + i * shade_width, y1, x1 + (i+1) * shade_width, shade_y2)

    
def draw():
    
    # Set adjacency amount to use
    adjacency = 30 + random(90)
    
    # Generate primary colour
    h, s, b = ColourGenerator.generate_random_hsb(s=50, b=50)
    
    # Draw primary colour box
    draw_box(0, 0, width, height/2, h, s, b)
    
    # Draw complementary colour box
    h_complement = ColourGenerator.get_complementary_hue(h)
    draw_box(0, height/2, width, 0.75 * height, h_complement, s, b)
    
    # Draw adjacent colour boxes
    h_left, h_right = ColourGenerator.get_adjacent_hues(h, adjacency)
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
    
    
    