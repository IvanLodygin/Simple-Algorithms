Q = 256
B = 13

def get_hash(string: str) -> int:
    length = len(string)
    res = 0
    
    for i in range(length):
        res  = (B*res + ord(string[i])) % Q
        
    return res

def search_patterns(pattern: str, text: str) -> list:
    result = list()
    
    text_length = len(text)
    pattern_length = len(pattern)
    
    multiplier = 1
    
    for _ in range(1, pattern_length):
        multiplier = (multiplier * B) % Q
    
    pattern_hash = get_hash(pattern)
    text_hash = get_hash(text[:pattern_length])
    
    for i in range(text_length - pattern_length + 1):
        if(pattern_hash == text_hash):
            if text[i: i + pattern_length] == pattern:
                result.append(i)
            
        if(i < text_length - pattern_length):
            text_hash = ((text_hash - ord(text[i]) * multiplier) * B + ord(text[i + pattern_length])) % Q
 
        if text_hash < 0:
            text_hash += Q
            
    return result
