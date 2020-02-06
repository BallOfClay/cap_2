import struct
# from data import n15w062.slope as byteString

sampleBytes = byteString[0:1000]

testBytes = b'\x00\x01\x00\x02'
testResult = struct.unpack('>HH', sampleBytes)
print(testResult)