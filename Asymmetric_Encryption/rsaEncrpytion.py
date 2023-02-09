import rsa
# The following is an example of assymetric in python using the RSA encrpytion algorithim


#Encryption Section
# Public Key is for Encrpytion
# Private Key is for Decrpytion

#Generate Keys
public_key, private_key = rsa.newkeys(1024)

# Creates Public and Private Keys
with open("public.pem", "wb") as f:
    f.write(public_key.save_pkcs1("PEM"))

with open("private.pem", "wb") as f:
    f.write(private_key.save_pkcs1("PEM"))


# Reads Public & Private Keys
with open("public.pem", "rb") as f:
    public_key = rsa.PublicKey.load_pkcs1(f.read())

with open("private.pem", "rb") as f:
    private_key= rsa.PrivateKey.load_pkcs1(f.read())

# Plaintext message
enMessage = "Hello my password is neural_nine999"

# Encrpyted Message with Public Key
encrpyted_message = rsa.encrypt(enMessage.encode(), public_key)

# Print encrypted message to textfile
with open("encrypted.message", "wb") as f:
    f.write(encrpyted_message)

# Decrypted message
decrypted_message = rsa.decrypt(encrpyted_message, private_key)

# Print encrypted message to textfile
with open("decrypted.message", "wb") as f:
    f.write(decrypted_message)


# Signature Section
# Uses SHA-256 as hashing function for signature

sigMesssage = "I have a new account on twitter which is @madeupname999"


# Generate Signature
signature = rsa.sign(sigMesssage.encode(), private_key, "SHA-256")

# Write Signature to text file
with open("signature", "wb") as f:
    f.write(signature)

# Read Signature from text file
with open("signature", "rb") as f:
    signature = f.read()

# Print verification of signature 
print(rsa.verify(sigMesssage.encode(), signature, public_key))
