student={
	'dimple' : 92,
	'harry' : 78,
	'jenny' : 67,
	'raju' : 32,
	'maya' : 53,

}
print(student)
student_with_grade ={}
for key,value in student.items():
	if value >91 and value <100:
		student_with_grade[key] = 'a+'
	elif value >81 and value <90:
		student_with_grade[key] = 'a'
	elif value >71 and value <80:
		student_with_grade[key] = 'b+'
	elif value >61 and value <70:
		student_with_grade[key] = 'b'
	elif value >51 and value <60:
		student_with_grade[key] = 'c'
	elif value >41 and value <50:
		student_with_grade[key] = 'd'
	else:
		student_with_grade[key] = 'f'
	
print(student_with_grade)

	
	