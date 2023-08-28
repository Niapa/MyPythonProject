"""Требуется найти в массиве list_1 самый близкий по величине элемент к заданному числу k и вывести его.

Пример:


list_1 = [1, 2, 3, 4, 5]
k = 6
# 5


for i in range(len(list_1)):
    if list_1[i] < k:
        nearest_num = -k
    else:
        nearest_num = nearest_num + 0
    if list_1[i] >= k and list_1[i] - k <= nearest_num - k:
        nearest_num = list_1[i]
    elif list_1[i] <= k and nearest_num - k <= list_1[i] - k:
        nearest_num = list_1[i]
print(nearest_num)

_________________
def find_closest_number(arr, target):
closest_number = 0
for num in arr:
diff = num - target
if diff < closest_number - target:
closest_number = num
return closest_number
closest_number = find_closest_number(list_1, k)
print(f"Ближайшее число к {k} в массиве {list_1} - {closest_number}")
________________

if (k <= arr[i]):
        return arr[i]
    if (k >= arr[i - 1]):
        return arr[i - 1]
list_1 = [1, 2, 3, 4, 5]
k = 6
a = 0
for i in list_1:
    а1 = list_1[i] - k
    if a1 > 0:
        a = a1"""
list_1 = [1, 2, 3, 4, 6]
k = 6

closest = None
min_diff = None

for num in list_1:
    if num > k:
        diff = num - k
    else:
        diff = k - num
    if min_diff is None or diff < min_diff:
        min_diff = diff
        closest = num

print(closest)








