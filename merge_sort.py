def merge_sort(arr):
    """
    Sorts a list of strings by string length in descending order (longest to shortest) using merge sort.
    """
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    return merge(left, right)

def merge(left, right):
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if len(left[i]) >= len(right[j]):
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result

# Test lists
list1 = ["apple", "banana", "cherry", "date", "elderberry", "fig", "grape", "honeydew", "kiwi", "lemon", "mango", "nectarine", "orange", "peach", "quince", "raspberry", "strawberry", "tangerine", "ugli", "vanilla"]
list2 = ["short", "medium length", "a very long string indeed", "tiny", "another medium one", "super long string with many words", "hi", "hello world", "python programming", "data structures and algorithms", "machine learning", "artificial intelligence", "computer science", "software engineering", "web development", "mobile apps", "cloud computing", "big data", "internet of things", "blockchain"]
list3 = ["a", "ab", "abc", "abcd", "abcde", "abcdef", "abcdefg", "abcdefgh", "abcdefghi", "abcdefghij", "abcdefghijk", "abcdefghijkl", "abcdefghijklm", "abcdefghijklmn", "abcdefghijklmno", "abcdefghijklmnop", "abcdefghijklmnopq", "abcdefghijklmnopqr", "abcdefghijklmnopqrs", "abcdefghijklmnopqrst"]

print("Original list1:", list1)
sorted_list1 = merge_sort(list1)
print("Sorted list1 (by length descending):", sorted_list1)

print("\nOriginal list2:", list2)
sorted_list2 = merge_sort(list2)
print("Sorted list2 (by length descending):", sorted_list2)

print("\nOriginal list3:", list3)
sorted_list3 = merge_sort(list3)
print("Sorted list3 (by length descending):", sorted_list3)
