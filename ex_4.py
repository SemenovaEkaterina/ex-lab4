from librip.decorators import print_result


@print_result
def test_1(a):
    return a


@print_result
def test_2():
    return 'iu'


@print_result
def test_3():
    return {'a': 1, 'b': 2}


@print_result
def test_4():
    return [1, 2]


test_1(1)
test_2()
test_3()
test_4()
