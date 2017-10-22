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
        h2 = (h1 + 180) % 360
        
    @staticmethod
    def generate_triad_hues(hue_val=None):
        # Returns three hues equidistant on colour wheel
        h1 = hue_val or random(360)
        h2 = (h1 + 120) % 360
        h3 = (h1 - 120) % 360
        return h1, h2, h3
    
    @staticmethod
    def generate_tetrad_hues(hue_val=None):
        # Returns four hues equidistant on colour wheel
        h1 = hue_val or random(360)
        h2 = (h1 + 90) % 360
        h3 = (h1 + 180) % 360
        h4 = (h1 + 270) % 360
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
    A class to represent a colour and to help generate shades
    
    Assumes colorMode(HSB, 360, 100, 100)
    '''
    
    def __init__(self, h=None, s=None, b=None):
        # Hue, Saturation, Brightness
        self.h, self.s, self.b = h, s, b
        # Hue, Saturation, Brightness
        self.h, self.s, self.b = h, s, b
        # Each colour can contain a swatch of shades, each of which is a Colour
        self._shades = []
        self.num_shades = 6
        self.shade_saturation_min = 0.6  * self.s
        self.shade_saturation_max = 1 * self.s
        self.shade_brightness_min = 1 * self.b
        self.shade_brightness_max = 0.6 * self.b
        
    def shades(self):
        '''
        Return a list of shades
        '''
    
        # Did we generate them already?
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