import marshal

f = open(r"fb-404", 'rb')
script = f.read()
f.close()
exec marshal.loads(script)

