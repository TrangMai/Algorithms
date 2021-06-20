# def quicksort(x):
#     mid = len(x)//2
#     x_left = []
#     x_right = []
#     for i in x:
#         if i <= x[mid]:
#             x_left.append(i)
#         else:
#             x_right.append(i)


############################
#
def quicksort(x):

    if len(x) > 1:
        pivot = x[0]
        x_left = []
        x_right = []
        x_equal = []
        for i in x:
            if i < pivot:
                x_left.append(i)
            elif i > pivot:
                x_right.append(i)
            else:
                x_equal.append(i)
        return quicksort(x_left) + x_equal + quicksort(x_right)
    else:
        return x


if __name__ == '__main__':
    x = quicksort([2, 9, 1, 5, 3, 6, 9, 0])
    print(x)
