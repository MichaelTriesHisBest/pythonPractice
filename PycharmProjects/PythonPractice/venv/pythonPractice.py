import random

randomlyfilledArray = random.sample(range(15), 15)

arbitraryArray = [1, 4, 5, 3, 6, 7, 14, -3]


class PythonPractice:
    """SORTING ALGORITHMS IN PYTHON"""


def bubbleSort(arr):
    """BUBBLE SORT IN PYTHON"""

    n = len(arr)

    for a in range(n - 1):

        for x in range(n - a - 1):
            if arr[x] > arr[x + 1]:
                arr[x + 1] = arr[x]

    print(arr)


"""END OF BUBBLE SORT IN PYTHON"""

"""SELECTIVE SORT IN PYTHON"""


def selectionSort(arr):
    lengthofArray = len(arr)

    for i in range(lengthofArray):
        # Find the minimum element in remaining
        # unsorted array
        min_idx = i
        for j in range(i + 1, lengthofArray):
            if arr[min_idx] > arr[j]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]

    print( arr)


"""END OF SELECTIVE SORT IN PYTHON"""


def insertionSort(arr):
    n = len(arr)
    for x in range(1, n):
        keyElement = arr[x]
        xx = x - 1
        while xx >= 0 and keyElement < arr[xx]:
            arr[xx + 1] = arr[xx]
            xx -= 1
        arr[xx + 1] = keyElement

    print(arr)


def whichSort(answer):
    default = "well shit"
    choices = {'selectionSort': selectionSort(arbitraryArray), 'bubbleSort': bubbleSort(arbitraryArray)
        , 'insertionSort': insertionSort(arbitraryArray)}
    choices.get(answer)

    # if 'bubble' in answer:
    #     bubbleSort(arbitraryArray)
    # elif 'select' in answer:
    #     selectionSort(arbitraryArray)
    # elif 'insert' in answer:
    #     insertionSort(arbitraryArray)
    # else:
    #     print('You must not want to have your stuff sorted huh')


def main():
    answer = input("Which sort would you like to use?")
    whichSort(answer)


if __name__ == '__main__':
    main()


