# lists are mutable while tuples are immutable

my_list = [1,2,3]

# print(my_list)

my_list2 = [4,5,6]

# my_list.append(my_list2) # [1,2,3,[4,5,6]]

# my_list.extend(my_list2) # [1,2,3,4,5,6]

# my_list.insert(0, 1) # [1, 1, 2, 3]

# my_list.insert(2, 4) # [1,2,4,3]

# my_list.insert(1, [1, 2, 3]) # [1, [1, 2, 3], 2, 3]

# print(max(my_list))

# print(sum(my_list))

courses = [ 'Math', 'CompSci', 'Science', 'Engineering']

# courses.remove('Science') # ['Math', 'CompSci', 'Engineering']

# print(courses.pop()) # 'Engineering'

# courses.pop()
# print(courses) [ 'Math', 'CompSci', 'Science']

# courses.reverse()

# courses.sort() #ascending

# courses.sort(reverse=True) #descending

# print(courses.index('Science'))

print('some' in courses)