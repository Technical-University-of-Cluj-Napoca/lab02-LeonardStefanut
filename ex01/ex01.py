def group_anagrams(strs: list[str]) -> list[list[str]]:
    
    mapp = {}
    
    for word in strs:
        sorted_key = "".join(sorted(word))
        
        if sorted_key in mapp:
            mapp[sorted_key].append(word)
        else:
            mapp[sorted_key] = [word]

    return list(mapp.values())



if __name__ == "__main__":
    input_strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
    result = group_anagrams(input_strs)
    print(result)  