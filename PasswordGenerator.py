#!/usr/bin/env python3
import random
class PasswordGenerator:
    # Character sets
    DIGITS = '0123456789'
    LOWERCASE = 'abcdefghijklmnopqrstuvwxyz'
    UPPERCASE = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    SYMBOLS = '!@#$%^&*()_+-=[]{}|;:,.<>?'
    
    def __init__(self):
        """Initialize the generator."""
        self.length = 0
        self.pool = ""
    
    def get_preferences(self):
        """Get user preferences one by one."""
        print("PASSWORD GENERATOR")
        
        # Get password length
        while True:
            try:
                self.length = int(input("\nEnter password length (8-128): "))
                if 8 <= self.length <= 128:
                    break
                print("Length must be between 8 and 128.")
            except ValueError:
                print("Please enter a valid number.")
        
        # Build character pool based on user choices
        self.pool = ""
        
        print("\nInclude digits (0-9)? (Y/N): ", end="")
        if input().strip().upper() in ['Y', 'YES']:
            self.pool += self.DIGITS
        
        print("Include lowercase letters (a-z)? (Y/N): ", end="")
        if input().strip().upper() in ['Y', 'YES']:
            self.pool += self.LOWERCASE
        
        print("Include uppercase letters (A-Z)? (Y/N): ", end="")
        if input().strip().upper() in ['Y', 'YES']:
            self.pool += self.UPPERCASE
        
        print("Include symbols (!@#$%^&*)? (Y/N): ", end="")
        if input().strip().upper() in ['Y', 'YES']:
            self.pool += self.SYMBOLS
        
        if not self.pool:
            print("Error: No character types selected!")
            return False
        return True
    
    def generate_passwords(self):
        """Generate 3 passwords."""
        passwords = []
        
        for option in range(3):
            password = ""
            for _ in range(self.length):
                # Get random character from pool
                random_index = random.randint(0, len(self.pool) - 1)
                password += self.pool[random_index]
            passwords.append(password)
        
        return passwords
    
    def display_results(self, passwords):
        """Display generated passwords."""
        print("YOUR PASSWORDS\n")
        
        for i, pwd in enumerate(passwords, 1):
            print(f"Option {i}: {pwd}")
        
        print("\n" + "-"*40)
        print(f"Length: {self.length} characters")
        print("Character types:", end=" ")
        
        types = []
        if any(c in self.DIGITS for c in self.pool):
            types.append("Digits")
        if any(c in self.LOWERCASE for c in self.pool):
            types.append("Lowercase")
        if any(c in self.UPPERCASE for c in self.pool):
            types.append("Uppercase")
        if any(c in self.SYMBOLS for c in self.pool):
            types.append("Symbols")
        print(", ".join(types))


def main():
    """Main function."""
    print("\nWelcome to Password Generator!")
    
    while True:
        generator = PasswordGenerator()
        
        if not generator.get_preferences():
            continue
        
        passwords = generator.generate_passwords()
        generator.display_results(passwords)
        
        again = input("Generate another set? (Y/N): ").strip().upper()
        if again not in ['Y', 'YES']:
            print("\nGoodbye!")
            break

if __name__ == "__main__":
    main()