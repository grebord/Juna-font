# run with python3 ./genGOADB.py Juna-Regular.sfd > GlyphOrderAndAliasDB
# from outside the nested enviro
import fontforge
import sys
font = fontforge.open(sys.argv[1])
for glyph in font.glyphs():
	print("{} {}".format(glyph.glyphname, glyph.glyphname))

