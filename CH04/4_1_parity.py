
# Time Complexity: O(n), where n is the total number of bits
def parity1(x: int) -> int:
    result = 0

    while x:
        result ^= x & 1
        x >>= 1
    return result

# Time Complexity: O(k), where k is the total number of bits which are 1
def parity2(x: int) -> int:
    result = 0
    while x:
        result ^= 1
        x &= x - 1
    return result

# Time Complexity: O(log(n))
def parity3(x: int) -> int:
    x ^= x >> 32
    x ^= x >> 16
    x ^= x >> 8
    x ^= x >> 4
    x ^= x >> 2
    x ^= x >> 1
    return x & 0x1

num = 5
print("Parity1: " + str(parity1(num)))
print("Parity2: " + str(parity2(num)))
print("Parity3: " + str(parity3(num)))