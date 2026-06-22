import hashlib

prompt = "Typing messages that you want to encode: "
data = input(prompt)

md5_data_hashed = hashlib.md5(data.strip().encode()).hexdigest()
sha1_data_hashed = hashlib.sha1(data.strip().encode()).hexdigest()
sha224_data_hashed = hashlib.sha224(data.strip().encode()).hexdigest()
sha256_data_hashed = hashlib.sha256(data.strip().encode()).hexdigest()
sha384_data_hashed = hashlib.sha384(data.strip().encode()).hexdigest()
sha512_data_hashed = hashlib.sha512(data.strip().encode()).hexdigest()
sha3_224_data_hashed = hashlib.sha3_224(data.strip().encode()).hexdigest()
sha3_256_data_hashed = hashlib.sha3_256(data.strip().encode()).hexdigest()
sha3_384_data_hashed = hashlib.sha3_384(data.strip().encode()).hexdigest()
sha3_512_data_hashed = hashlib.sha3_512(data.strip().encode()).hexdigest()

print(f"\nMD5 Hash: {md5_data_hashed}\nSHA1 Hash: {sha1_data_hashed}\nSHA224 Hash: {sha224_data_hashed}\nSHA256 Hash: {sha256_data_hashed}\nSHA384 Hash: {sha384_data_hashed}\nSHA512 Hash: {sha3_512_data_hashed}\nSHA3_224 Hash: {sha3_224_data_hashed}\nSHA3_256 Hash: {sha3_256_data_hashed}\nSHA3_384 Hash: {sha3_384_data_hashed}\nSHA3_512 Hash: {sha3_512_data_hashed}")
