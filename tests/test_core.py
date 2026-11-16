from oneplusone import one_plus_one


def test_one_plus_one_is_two():
    assert one_plus_one() == 2
    assert type(one_plus_one()) is int
