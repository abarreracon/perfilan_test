"""
// Dividir array en el tamaño que se le pasa en el segundo parámetro.
// --- Directions
// Given an array and chunk size, divide the array into many subarrays
// where each subarray is of length size
// --- Examples
// chunk([1, 2, 3, 4], 2) --> [[ 1, 2], [3, 4]]
// chunk([1, 2, 3, 4, 5], 2) --> [[ 1, 2], [3, 4], [5]]
// chunk([1, 2, 3, 4, 5, 6, 7, 8], 3) --> [[ 1, 2, 3], [4, 5, 6], [7, 8]]
// chunk([1, 2, 3, 4, 5], 4) --> [[ 1, 2, 3, 4], [5]]
// chunk([1, 2, 3, 4, 5], 10) --> [[ 1, 2, 3, 4, 5]]
"""

def chunk(lst: list, size: int) -> list: # 2014.493ms
    chunked = []

    for element in lst:
        if not chunked:
            chunked.append([])
        last_chunk = chunked[-1]
        if len(last_chunk) == size:
            last_chunk = []
            chunked.append(last_chunk)
        last_chunk.append(element)

    return chunked

print(chunk([1, 2, 3, 4], 2))


