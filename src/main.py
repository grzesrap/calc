#!/usr/bin/python3

import array as arr
import os
import redis

id = 123
idName = "out_" + str(id)

redisHost = os.environ.get('REDIS_HOST')
inputFileName = 'input/in.json'
outputFileNane = 'output/' + idName + '.json'

redis_server = redis.Redis(redisHost)
redis_server.set("test", "OK")

inputFile = open(inputFileName, 'r') 
Lines = inputFile.readlines() 

numbers = arr.array('d', [0, 0, 0])  
count = 0

for line in Lines:
    numbers[count] = float(line.strip())
    count += 1

numbers[2] = numbers[0] + numbers[1]

# save in file
with open(outputFileNane, 'w') as f:
    print(numbers[2], file=f)

# save in redis
redis_server.set(idName, numbers[2])

print(numbers[-1])
