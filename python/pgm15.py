my_dict = {'banana': 3,'apple': 1,'cherry': 2, 'dates': 4}
print("original list:", my_dict)
assorted_dict = dict(sorted(my_dict.items()))
print("ascending order:",assorted_dict)
dsorted_dict = dict(sorted(my_dict.items(), reverse=True))
print("descending order:",dsorted_dict)
