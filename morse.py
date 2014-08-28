'''
Author:		Ryan Wagner
Date:		August 28, 2014
Description:	morse.py - translates input phrase into output morse code,
		then into an audio morse output.
		Use in Dailyprogrammer Intermediate #177.
'''
import wave, math, struct

def out_morse(phrase):
	fname = wave.open( "cat.wav", "w" )
	fname.setparams( ( 1 , 2 , 1000, 0 , 'NONE', 'noncompressed' ) )
	freq = { '.' : 440.0, '-' : 550.0, '_' : 10.0, ' ' : 10.0 }
	for i in range( len( phrase ) ):
		for j in range( 0, 400 ):
			tone = math.sin( math.pi * 2 * freq[ phrase[ i ] ] *
				j / 1000 )
			volume = 32767 * tone
			fname.writeframes( struct.pack( 'h', int( volume ) ) )
		for j in range( 0 , 100 ):
			fname.writeframes( struct.pack( 'h', 0 ) )
	
	fname.close( )

words = { 'a' : '.-', 'b' : '-...', 'c' : '-.-.', 'd' : '-..', 'e' : '.', \
	'f' : '..-.', 'g' : '--.', 'h' : '....', 'i' : '..', 'j' : '.---', \
	'k' : '-.-', 'l' : '.-..', 'm' : '--', 'n' : '-.', 'o' : '---', \
	'p' : '.--.', 'q' : '--.-', 'r' : '.-.', 's' : '...', 't' : '-', \
	'u' : '..--', 'v' : '...-', 'w' : '.--', 'x' : '-..-', 'y' : '-.--', \
	'z' : '--..', ' ' : '_'}
try:
	in_str = str( raw_input( '>' ) )
	phrase = ''
	for x in in_str:
		phrase += words[ x.lower() ] + ' '
	print phrase
	out_morse(phrase)
except KeyError as desc:
	print 'Invalid input (', desc, ')'
