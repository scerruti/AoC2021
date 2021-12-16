import collections
import re
import math


def main(file):
    with open(file, 'r') as f:
        lines = f.readlines()

    for line in lines:
        line = line.strip()
        binary = ''.join([format(int(char,16), '04b') for char in line])

        print(process(binary))


def literal(packet):
    value = ''
    position = 0
    done = False
    while not done:
        done = packet[position] == '0'
        value += packet[position+1:position+5]
        position += 5

    position += 6 # header
    return position, int(value, 2)


def total_length(packet):
    length = int(packet[:15], 2)
    subpackets = packet[15:]
    position = 0
    result = []
    version_sum = 0

    while position < length:
        v, (p, r) = process(subpackets[position:])
        position += p
        version_sum += v
        result.append(r)
    return version_sum, (position + 22, result)


def number_of_packets(packet):
    length = int(packet[:11], 2)
    subpackets = packet[11:]
    position = 0
    result = []
    version_sum = 0

    for _ in range(length):
        v, (p, r) = process(subpackets[position:])
        position += p
        version_sum += v
        result.append(r)
    return version_sum, (position + 18, result)

"""
Packets with type ID 0 are sum packets - their value is the sum of the values of their sub-packets. If they only have a single sub-packet, their value is the value of the sub-packet.
Packets with type ID 1 are product packets - their value is the result of multiplying together the values of their sub-packets. If they only have a single sub-packet, their value is the value of the sub-packet.
Packets with type ID 2 are minimum packets - their value is the minimum of the values of their sub-packets.
Packets with type ID 3 are maximum packets - their value is the maximum of the values of their sub-packets.
Packets with type ID 5 are greater than packets - their value is 1 if the value of the first sub-packet is greater than the value of the second sub-packet; otherwise, their value is 0. These packets always have exactly two sub-packets.
Packets with type ID 6 are less than packets - their value is 1 if the value of the first sub-packet is less than the value of the second sub-packet; otherwise, their value is 0. These packets always have exactly two sub-packets.
Packets with type ID 7 are equal to packets - their value is 1 if the value of the first sub-packet is equal to the value of the second sub-packet; otherwise, their value is 0. These packets always have exactly two sub-packets.
"""


def packet_sum(length_function, packet):
    version_sum, (position, result) = length_function(packet)
    return version_sum, (position, sum(result))


def packet_product(length_function, packet):
    version_sum, (position, result) = length_function(packet)
    return version_sum, (position, math.prod(result))


def packet_minimum(length_function, packet):
    version_sum, (position, result) = length_function(packet)
    return version_sum, (position, min(result))


def packet_maximum(length_function, packet):
    version_sum, (position, result) = length_function(packet)
    return version_sum, (position, max(result))


def packet_greater(length_function, packet):
    version_sum, (position, result) = length_function(packet)
    return version_sum, (position, 1 if result[0] > result[1] else 0)


def packet_less(length_function, packet):
    version_sum, (position, result) = length_function(packet)
    return version_sum, (position, 1 if result[0] < result[1] else 0)


def packet_equal(length_function, packet):
    version_sum, (position, result) = length_function(packet)
    return version_sum, (position, 1 if result[0] == result[1] else 0)


operator = {
    0: packet_sum,
    1: packet_product,
    2: packet_minimum,
    3: packet_maximum,
    5: packet_greater,
    6: packet_less,
    7: packet_equal
}
length_id = {
    '0': total_length,
    '1': number_of_packets
}


def process(binary, version_sum=0):
    version_sum += int(binary[:3], 2)

    packet_type = int(binary[3:6], 2)
    if packet_type == 4:
        return version_sum, literal(binary[6:])
    else:
        length_type = binary[6]
        v, (position, result) = operator[packet_type](length_id[length_type], binary[7:])
        version_sum += v
        return version_sum, (position, result)


if __name__ == '__main__':
    main('input.txt')
