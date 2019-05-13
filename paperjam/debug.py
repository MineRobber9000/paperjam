import logging

logger = logging.Logger("paperjam")
fh = logging.FileHandler("paperjam.log")
fh.setLevel(logging.DEBUG)
ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)
format = logging.Formatter("%(name)24s - %(levelname)s: %(message)s")
fh.setFormatter(format)
ch.setFormatter(format)
logger.addHandler(fh)
logger.addHandler(ch)

def setLevel(level):
	level = getattr(logging,level.upper())
	fh.setLevel(level)
	ch.setLevel(level)

def log(lvl,x):
	getattr(logger,lvl.lower(),lambda x: x)(x)
