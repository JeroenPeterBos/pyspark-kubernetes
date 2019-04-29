import os

def find_all(name, path):
    result = []
    for root, dirs, files in os.walk(path):
        if name in files:
            result.append(os.path.join(root, name))
    return result

print("FOUND:" + str(find_all("demo.py", "/")))

f = open("file:///home/jeroen/Documents/Leap/boldeagle/examples/demo.py")

print(f.read())

print("END")
