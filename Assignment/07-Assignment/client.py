from xmlrpc.client import ServerProxy

client = ServerProxy("http://localhost:8001/")
result = client.add(10, 5)
print("Result: ", result)
