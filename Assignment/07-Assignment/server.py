from xmlrpc.server import SimpleXMLRPCServer

def add(x, y):
	return x + y

server = SimpleXMLRPCServer(("localhost", 8001))
server.register_function(add, "add")
print("Server is listening on Port 8001")
server.serve_forever()
