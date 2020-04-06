#
# Use Imagemagick to generate colored tokens from black tokens.
#

import os

TOKENS = [
# "donkey",
# "wagon",
# "truck",
# "raft",
# "rowboat",
# "steamship",
# "disc",
"home",
# "wall",
"wonder",
]

COLORS = [
    ("green",  "ForestGreen"), #228B22 rgb( 50, 129, 75)
    ("blue",   "RoyalBlue1"),  #4876FF rgb( 72, 118, 255)
    ("red",    "red2"),        #EE0000 rgb(238, 0, 0)
    ("yellow", "yellow2"),     #EEEE00 	rgb(238, 238, 0)
    ("grey",   "grey66"),      #A9A9A9 rgb(168, 168, 168)
    ("black",  "grey20"),      #333333 rgb( 51, 51, 51)
    ("white",  "grey98"),      #FAFAFA rgb(250, 250, 250)
]

for token in TOKENS:
  for filename,colorname in COLORS:
    cmd = "convert input_assets/{token}.png -fuzz 10% -fill {colorname} -opaque black output_assets/{token}_{filename}.png".format(**locals())
    print(cmd)
    os.system(cmd)
