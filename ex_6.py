#!/usr/bin/env python3
import json
import sys
from librip.ctxmngrs import timer
from librip.decorators import print_result
from librip.gen import field, gen_random
from librip.iterators import Unique as unique

path = sys.argv[1]

with open(path) as f:
    data = json.load(f)



@print_result
def f1(arg):
    return sorted(unique(field(data, "job-name"), ignore_case = True), key = lambda x: x.lower())


@print_result
def f2(arg):
    return list(filter(lambda x: x[0:11].lower() == "программист", arg))


@print_result
def f3(arg):
    return list(map(lambda x: x + " с опытом Python", arg))


@print_result
def f4(arg):
    return [x + ", зарплата " + str(y) + " руб." for x, y in zip(arg, gen_random(100000, 200000, len(arg)))]


with timer():
    f4(f3(f2(f1(data))))

