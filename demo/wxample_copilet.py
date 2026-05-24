def is_palindrome(s):
    """Return True if the string is a palindrome, otherwise False."""
    normalized = s.lower()
    return normalized == normalized[::-1]

# Example usage
if __name__ == '__main__':
    print(is_palindrome('radar'))  # True
    print(is_palindrome('hello'))  # False
