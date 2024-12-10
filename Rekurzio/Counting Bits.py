def count_one_bits(n):
    count = 0
    bit_position = 0
    
    while (1 << bit_position) <= n:
        block_size = 1 << (bit_position + 1)
        
        full_blocks = (n + 1) // block_size
        
        count += full_blocks * (block_size // 2)
        
        remainder = (n + 1) % block_size

        count += max(0, remainder - (block_size // 2))
        
        bit_position += 1
    
    return count

n = int(input())
print(count_one_bits(n))