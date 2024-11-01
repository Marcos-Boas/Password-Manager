# native python library for dealing with strings 
import string

# native python library for generating cryptographically strong random numbers 
import secrets

# provides hash functions for various algorithms, such as MD5 and SHA-1
import hashlib

# native python library, allows you to encode data in Base16, Base32, Base64 and Base85 and decode it. 
import base64

# native python library, helps manipulate directories
from pathlib import Path

# native python library, allows data encryption 
from cryptography.fernet import Fernet, InvalidToken

# class name based on a encryption hash algorithm (fernet)
class FernetHasher:
    # class variables, and constants
    RANDOM_STRING_CHARS = string.ascii_lowercase + string.ascii_uppercase
    BASE_DIR = Path(__file__).resolve().parent.parent
    KEY_DIR = BASE_DIR / 'keys'
    
    # constructor method, required to have specifically that name
    # self is for instance methods, unlike cls  
    def __init__(self, key):
        if not isinstance(key, bytes):
            key = key.encode()

        self.fernet = Fernet(key)
        
        
    # class methods must be signaled with '@classmethod' and accompanied by a 'cls'
    @classmethod
    def _get_random_string(cls, length=25): # declaring a parameter and setting its default value 
        string = ''
        for i in range(length):
           string += secrets.choice(cls.RANDOM_STRING_CHARS)
           
        return string


    @classmethod
    def create_key(cls, archive=False):
        value = cls._get_random_string()
        
        hasher = hashlib.sha256(value.encode('utf-8')).digest()
        key = base64.b64encode(hasher)
        
        if archive:
            return key, cls.archive_key(key)
        
        return key, None
        
    
    @classmethod
    def archive_key(cls, key):
        file = 'key.key'
        
        while Path(cls.KEY_DIR / file).exists():
            # how to interpolate texts
            file = f'key_{cls._get_random_string(length=5)}.key'        
        
        
        # creating a context and defining how the file will be opened, w = write | b = binary 
        with open(cls.KEY_DIR / file, 'wb') as arq:
             arq.write(key)
             
        return cls.KEY_DIR / file
    
    
    def encrypt(self, value):
        if not isinstance(value, bytes):
            value = value.encode()

        return self.fernet.encrypt(value)
             
             
    def decrypt(self, value):
        if not isinstance(value, bytes):
            value = value.encode()
            
        try:      
            return self.fernet.decrypt(value).decode()
        except InvalidToken as e:
            print("Token inválido")
        