import sys, time, logging, getch
from cops_and_robots.Cop import Cop

logger = logging.getLogger('moveTest')
logging.basicConfig(level=logging.DEBUG)

cop = Cop('Deckard')
OPCODE = cop.OPCODE

cop.ser.write(chr(OPCODE['start']) + chr(OPCODE['full']))

step = 100
cop.speed = 0
cop.radius = 0
x = 'a'

keymap = {  '.' : cop.faster,
			',' : cop.slower,
			'w' : cop.forward,
			's' : cop.backward,
			'a' : cop.left,
			'd' : cop.right,
			' ' : cop.stop }

tstep = 0.5

while x != 'z':
	x = getch.getch()
	logging.info('char: %s',x)

	cmd = cop.move()
	cop.ser.write(cmd)
	time.sleep(tstep)

ser.close()