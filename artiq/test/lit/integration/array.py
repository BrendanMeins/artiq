# RUN: %python -m artiq.compiler.testbench.jit %s
# REQUIRES: exceptions

ary = array([1, 2, 3])
assert len(ary) == 3
assert ary.shape == (3,)
assert [x * x for x in ary] == [1, 4, 9]

# Reassign to an existing value to disambiguate type of empty array.
empty_array = array([1])
empty_array = array([])
assert len(empty_array) == 0
assert empty_array.shape == (0,)
assert [x * x for x in empty_array] == []

matrix = array([[1.0, 2.0, 3.0], [4.0, 5.0, 6.0]])
assert len(matrix) == 2
assert matrix.shape == (2, 3)
assert matrix[0][0] == 1.0
assert matrix[0][1] == 2.0
assert matrix[0][2] == 3.0
assert matrix[1][0] == 4.0
assert matrix[1][1] == 5.0
assert matrix[1][2] == 6.0
# FIXME: Need to decide on a solution for array comparisons —
# NumPy returns an array of bools!
# assert [x for x in matrix] == [array([1.0, 2.0, 3.0]), array([4.0, 5.0, 6.0])]

three_tensor = array([[[1.0, 2.0, 3.0], [4.0, 5.0, 6.0]]])
assert len(three_tensor) == 1
assert three_tensor.shape == (1, 2, 3)
