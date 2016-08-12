name = ['Rick', 'Leo', 'Frank', 'Josh', 'Sarah', 'Marc']

input_name = input('Please input name: ').title()
result_name = []

for n in name:
    if n[0:len(input_name)] == input_name:
        result_name.append(n)

if len(result_name) != 0:
    print('The name is %s' % result_name)
else:
    print('There is not %s' %(input_name))