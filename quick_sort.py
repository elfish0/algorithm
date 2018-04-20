
def quick_sort(li, low, high):
    left = low
    right = high
    if left < right:
        key = li[left]
        while left < right:
            while left < right and li[right] >= key:
                right -= 1
            li[left], li[right] = li[right], li[left]
            while left < right and li[left] <= key:
                print(left)
                left += 1
            li[left], li[right] = li[right], li[left]
        print("一次任务结束", li)

        quick_sort(li, low, left-1)
        quick_sort(li, right+1, high)

t = [3, 1, 2, 4, 2, 0, 5, 3, 7, 9, 8]
quick_sort(t, 0, len(t)-1)
