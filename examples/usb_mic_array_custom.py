"""
Control pixel ring on ReSpeaker USB Mic Array
"""

import time

from pixel_ring import pixel_ring


if __name__ == '__main__':
	pixel_ring.trace()
	# first color = active, second color = inactive 
	pixel_ring.set_color_palette(0x400000, 0x000000)
