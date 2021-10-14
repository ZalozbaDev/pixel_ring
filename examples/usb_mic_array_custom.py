"""
Control pixel ring on ReSpeaker USB Mic Array
"""

import time

from pixel_ring import pixel_ring


if __name__ == '__main__':
	pixel_ring.trace()
	pixel_ring.set_color_palette(0xFF0000, 0x00FF00)
