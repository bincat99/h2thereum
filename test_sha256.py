import hashlib


i = 0

for i in xrange (10000000):
  s = "H2thereum" + str (i)
  h = hashlib.sha256 (s).hexdigest()

  if h[:3] == "000":
    print "sha256 (\"H2thereum\" + \"{}\") == 0x{}".format (i, h)
