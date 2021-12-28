import os
import json
import boto3

if not os.path.exists("cache"):
    os.mkdir("cache")


if not os.path.exists("cache/old_files"):
    os.mkdir("cache/old_files")


if not os.path.exists("functions.json"):
    raise RuntimeError("You need to have a \"functions.json\" file!")


with open("functions.json", "r") as f:
    functions = json.load(f)


print(functions)
