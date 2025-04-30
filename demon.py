import os
import sys


def files(*args):
    dct = {"input": args[0], "output": args[1], "max_depth": 0}

    if len(args) == 3:
        dct["max_depth"] = int(args[2]) - 1
    for paths in os.walk(dct["input"]):
        path = paths[0].replace(dct["input"], '').split('/')
        to_copy_path = dct["output"]
        for i in path[len(path) - dct["max_depth"]:]:
            to_copy_path += "/"
            to_copy_path += i
            os.system("mkdir -p {0}".format(to_copy_path))
        for i in paths[2]:
            os.system(
                "cp {input} {output}".format(
                    input=paths[0] + "/" + i,
                    output=to_copy_path + "/"
                )
            )

files(*sys.argv[1:])