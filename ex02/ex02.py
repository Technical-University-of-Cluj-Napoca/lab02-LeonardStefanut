def multiply_all(*args: int) -> int:
    
    product = 1
    
    for num in args:
        product *= num
        
    return product

if __name__ == "__main__":
    result = multiply_all(1, 2, 3, 4)
    print(result)
    