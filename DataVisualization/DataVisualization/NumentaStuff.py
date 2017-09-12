import bitarray as ba
bitthing = [1,0,0,1]

bitotherthing = [1,0,1,0]
#bitwise and: &
#bitwise or: |
#bitwise Xor: ^
# bitwise invert: ~invert


bitotherthing = ba.bitarray(bitotherthing)
print (bitotherthing)

print(bitthing)
print(bitotherthing)
print()
print(ba.bitarray(bitthing) & ba.bitarray(bitotherthing))
print(ba.bitarray(bitthing) | ba.bitarray(bitotherthing))
print(ba.bitarray(bitthing) ^ ba.bitarray(bitotherthing))
print(ba.bitarray(bitthing) + ba.bitarray(bitotherthing))
print(~ ba.bitarray(bitotherthing))
print(bitotherthing.)


