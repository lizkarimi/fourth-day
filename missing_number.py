def find_missing(arr1, arr2):
    if len(arr1)==0 or len(arr2)==0:
        return 0
    if len(arr1)==len(arr2):
        return 0

    # Set longer array to lst1, shorter to lst2 
    if len(arr1) > len(arr2):
        lst1 = arr1
        lst2 = arr2
    else:
        lst1 = arr2
        lst2 = arr1

    # Go through elements in longer list
    for element in lst1:

        # If this element is not in lst2, we found it, return result
        if element not in lst2:
            return element

if __name__ == '__main__':
    print find_missing([1,2,3],[1,3,2])            