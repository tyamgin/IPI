import sys, math, os


def at(a, i):
    return a[i] if i in a else 0


def inc(dictionary, key, value=1):
    if key in dictionary:
        dictionary[key] += value
    else:
        dictionary[key] = value


def getOutput(path):
    if path:
        return open(path, 'w')
    return sys.stdout


def getInput(path):
    if path:
        return open(path, 'r')
    return sys.stdin


def closeOutput(stream):
    if stream != sys.stdout:
        stream.close()


def closeInput(stream):
    if stream != sys.stdin:
        stream.close()


def filePut(path, content):
    stream = getOutput(path)
    stream.write(content)
    closeOutput(stream)


def fileGet(path):
    stream = getInput(path)
    result = '\n'.join(stream.readlines())
    closeInput(stream)
    return result


def ne(a):
    return [e for e in a if e]


def scalarMul(a, b):
    return sum([a[i] * b[i] for i in range(len(a))])


def getAngleBetween(a, b):
    return math.acos(scalarMul(a, b) / math.sqrt(scalarMul(a, a)) / math.sqrt(scalarMul(b, b)))


def enumerateFiles(dir):
    return [os.path.join(dir, f)
            for f in os.listdir(dir)
            if os.path.isfile(os.path.join(dir, f))]