def search_loop(callback_function):
    
    while True:
        prefix = input("search> ")
        
        if prefix == ':q':
            break
            
        if prefix:
            results = callback_function(prefix)
            for res in results:
                print(res)