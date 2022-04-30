from test_framework import generic_test


def parity(x: int) -> int:
    # Soln 1: Using XOR
    # TC: O(n) where n represents total number of bits
    """
    num_bits = 0

    while x:
        '''
        XOR -> false, if both are same
        1 ^ 0 -> 1
        0 ^ 1 -> 1
        0 ^ 0 -> 0
        1 ^ 1 -> 0
        '''
        num_bits ^= x & 1
        x >>= 1

    return num_bits
    """

    # Soln 2: Using x & (x-1) property
    # TC: O(k) where k represents number of set bits
    """
    result = 0
    while x:
        '''
        x & (x-1) -> Erase lowest set bit
        x & ~(x-1) -> Erase all set bits, except lowest set bit
        '''
        result ^= 1
        x = x & (x-1)

    return result
    """

    # Soln 3:
    # TC:


if __name__ == '__main__':
    exit(generic_test.generic_test_main('parity.py', 'parity.tsv', parity))
