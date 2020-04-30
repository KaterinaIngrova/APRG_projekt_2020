odpoved = "Cau, jak se mas?"
import numpy
matrix = numpy.array([["C", " ", " ","m"],["a", "j", "s", "a"], ["u", "a", "e","s"],[",", "k", " ", "?"]])
print(matrix)

#prevod do dec.
dec_matrix = []
for list in matrix:
    for pismeno in list:
        dec_matrix.append(ord(pismeno))
print(dec_matrix)

dec_matrix = numpy.array([[67, 32, 32, 109], [97, 106, 115, 97], [117, 97, 101, 115], [44, 107, 32, 63]])
print(dec_matrix)

#prevod do hex.
hex_matrix0 = []
for list in dec_matrix:
    for cislo in list:
        hex_matrix0.append(hex(cislo))
print(hex_matrix0)

a = hex_matrix0[0:4]
b = hex_matrix0[4:8]
c = hex_matrix0[8:12]
d = hex_matrix0[12:]
hex_matrix = zip(a,b,c,d)
print(hex_matrix)
print(tuple(hex_matrix))

#prevod do bin
bin_matrix1 = []
for cislo in hex_matrix0:
    bin_matrix1.append(bin(int(cislo, 16)))
print(bin_matrix1)

a = bin_matrix1[0:4]
b = bin_matrix1[4:8]
c = bin_matrix1[8:12]
d = bin_matrix1[12:]
bin_matrix = zip(a,b,c,d)
print(bin_matrix)
print(tuple(bin_matrix))

#xor
key = 0b010101
xor_prepis = ()
def logical_xor(bin_matrix1, key):
    for cislo in bin_matrix1:
        xor_prepis = bool(cislo in bin_matrix1) ^ bool(key)
        return xor_prepis
logical_xor(bin_matrix1,key)

#subbytes
def subBytes(xor_prepis):
    for i in range(len(xor_prepis)):
        xor_prepis[i] = array[xor_prepis[i]]
subBytes(xor_prepis)

if __name__ == "__main__":
    main()