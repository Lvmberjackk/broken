import sys

"""On different devices app size is also different, 
	so i located triggers on mine and devided it by window size on my pc,
	in game this coefficients are multiplied by actual window size to get correct coordinates"""

CLICK_LIMIT = 2.0
for arg in sys.argv:
	if '--click-limit' in arg:
		CLICK_LIMIT = float(arg.split('=')[1])


DEV_SCREEN_SIZE_CONST = (450, 750)

APPLICATION_NAME = 'TelegramDesktop'

DEFAULT_COLOR_TRIGGER = {
    "red": {"min": 250, "max": 255},
    "green": {"min": 70, "max": 75},
    "blue": {"min": 120, "max": 125},
}


APPLICATION_TRIGGER = {
    "color": (254, 72, 123),  # Specific RGB color for game running detection
    "positions": [
        (440 + (60 / 402) * 100, 0 + (112 / 712) * 750),
        (440 + (43 / 402) * 100, 0 + (110 / 712) * 750),
        (440 + (102 / 402) * 100, 0 + (113 / 712) * 750),
        (440 + (61 / 402) * 100, 0 + (106 / 712) * 750),
    ],
}


PIXELS_PER_ITERATION = 10

NEW_GAME_TRIGGER_POS = (657, 589)  # Absolute position



BOMB_COLOR_TRIGGER = {
					"red":{"min":125, "max":140},
					"green":{"min":125, "max":135},
					"blue":{"min":125, "max":135}}

AVG_GAME_DURATION = 30

HELP_STRING = \
"""
Usage: main.py [AMOUNT OF GAMES] [OPTIONS]

Options:
	--help           - show this string
	--halloween      - enable halloween mode
	--elections      - enable elections mode
	--disable-dogs   - don't collect dogs
	--click-limit=n  - limit clicks (Example: --click-limit=0.05, only 5% of clicks)

Keybidings:
	1 - decrease clicks limit
	2 - increase clicks limit
"""
