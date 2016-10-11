# Created by Adrian Krige - 13/09/2016
import sys
import math

# Instantiate variables
# Instantiate all the L1 variables
l2 = False
file_name = str(sys.argv[1])
num_of_blocks = int(sys.argv[2])
size = int(sys.argv[3])
index_length = int(math.log(num_of_blocks, 2))
offset_length = int(math.log(size, 2))
block = [0] * num_of_blocks
misses = hits = cycles = 0

# If L2 cache is to be used instantiate L2 variables
if int(str(sys.argv[4])) is not 0:
    l2 = True
    num_of_blocks_2 = int(sys.argv[4])
    size_2 = int(sys.argv[5])
    index_length_2 = int(math.log(num_of_blocks_2, 2))
    offset_length_2 = int(math.log(size_2, 2))
    block_2 = [0] * num_of_blocks_2
    misses_2 = hits_2 = 0

# Read all lines of the given file into list
with open(file_name) as f:
    content = f.readlines()

# Loop though all elements in the list
for x in content:
    # Initialise L1 variables for current line
    address = "{0:016b}".format(int(x, 16))
    index = int(address[-(offset_length + index_length):-offset_length], 2)
    tag = address[0:-(offset_length + index_length)]

    # Initialise needed variables for l2
    if l2:
        index_2 = int(address[-(offset_length_2 + index_length_2):-offset_length_2], 2)
        tag_2 = address[0:-(offset_length_2 + index_length_2)]

    # Check if tags are the same at cache index
    if block[index] == tag:
        hits += 1
        cycles += 10

    # Check L2, or fetch from RAM
    else:
        misses += 1

        # Check in L2
        if l2:
            # Index in L2 contains address
            if block_2[index_2] == tag_2:
                hits_2 += 1
                cycles += 100
            # Miss in L2
            else:
                misses_2 += 1
                cycles += 1000
                block_2[index_2] = tag_2
        else:
            cycles += 1000

        block[index] = tag

# Calculate the CPI
print("Addresses: " + str(misses + hits))
print("\n")


miss_rate_1 = float(misses)/(misses+hits)
CPI_1 = 1 + (miss_rate_1 * 1000)
if l2:
    miss_rate_2 = (float(misses_2)/(misses_2+hits_2))
    CPI_2 = 1 + (miss_rate_1 * 100) + (miss_rate_1 * miss_rate_2 * 1000)

# Print results
print("L1 Hits:\t" + str(hits) + "\nL1 Misses:\t" + str(misses))
if l2:
    print("L2 Hits:\t" + str(hits_2) + "\nL2 Misses:\t" + str(misses_2))
print("Cycles: \t" + str(cycles) + "\nL1 CPI: \t\t" + str(CPI_1))
if l2:
    print("L2 CPI: \t\t" + str(CPI_2) + "\nPerformance ratio: \t" + str(CPI_1/CPI_2))
