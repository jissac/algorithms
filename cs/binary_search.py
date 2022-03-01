## BINARY SEARCH
## https://realpython.com/binary-search-python/
## time space complexity: https://iq.opengenus.org/time-complexity-of-binary-search/


from __future__ import annotations

def binary_search(items: list[int],value: int)->int | None:
    # find upper, middle, and lower boundaries
    left, right = 0, len(items) - 1
    

    while left <= right: 
        mid = (left + right) // 2
        if value == items[mid]:
            print(f"value: {value}, index: {mid}")
            return mid
        elif value > items[mid]:
            left = mid + 1
        elif value < items[mid]:
            right = mid - 1
    print ("Value not in list of items")
    return None
    
if __name__ == "__main__":
    input = [1,2,3,4,5]
    binary_search(input,4)