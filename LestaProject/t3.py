"""
Самым быстрым будет либо встроенная функция "sorted", либо метод списка "sort".
Они оба используют алгоритм "Timsort", который превосходно работает как на почти отсортированных массивах, так и неотсортированных.
"Timsort" имеет временную сложность O(n log n) в худшем случае и O(n) в лучшем(когда массив почти отсортирован).
Благодаря тому, что эта сортировка совмещает в себе "Merge Sort" и "Insertion Sort" на реальных данных она похволяет добиться наилучшей производительности.
"""