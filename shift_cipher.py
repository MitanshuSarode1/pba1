def shift_cipher_encrypt(text, shift):
    encrypted_text = ""
    
    for char in text:
        if char.isalpha():  
            shift_base = ord('A') if char.isupper() else ord('a')
            encrypted_char = chr((ord(char) - shift_base + shift) % 26 + shift_base)
        else:
            encrypted_char = char 
        
        encrypted_text += encrypted_char

    return encrypted_text


message = "GOOD MORNING"
shift_value = 5

encrypted_message = shift_cipher_encrypt(message, shift_value)
print("Encrypted Message:", encrypted_message)
