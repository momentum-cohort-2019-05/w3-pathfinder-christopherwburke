def read_line_of_ints(text):
    ints = []
    ints_as_strs = split_line(text)
    for int_as_str in ints_as_strs:
        ints.append(int(int_as_str))
    return ints

def split_line(line):
    return line.split()

def test_can_read_line_of_ints():
    text = "10 12 9 345 2 78"
    assert read_line_of_ints(text) == [10, 12, 9, 345, 2, 78]