"""The NNTP handler and server.

The handler uses infile/outfile for easy testing.

The server uses listen and accept along with conn.makefile."""

from paperjam import debug

def debug_msg(prefix,msg):
	debug.log("debug","{} {}".format(prefix,msg))

def debug_in(line):
	debug_msg("<",line)

def debug_out(line):
	debug_msg("<",line)

class NNTPServer:
	def __init__(self,infile,outfile):
		self.infile = infile
		self.outfile = outfile
	def readlines(self):
		while True:
			l = self.infile.readline()
			if not l: break
			l = l.rstrip("\r\n")
			debug_in(line)
			yield l
	def writeline(self,line):
		debug_out(line)
		self.outfile.write(line.strip("\r\n")+"\r\n")
		self.outfile.flush()
	def writelines(self,lines):
		if type(lines)==str: lines=lines.splitlines()
		for line in lines:
			self.writeline(line)
	def handleMessages(self):
		try:
			for line in self.readlines():
				tokens = re.split(r"\s+",line)
				if not tokens:
					self.writeline("501 You didn't format your lines correctly.")
