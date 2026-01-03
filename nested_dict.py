def add(name,roll,age,course,s):
	d={}
	d["Name"] = name
	d["Rollno"] = roll
	d["Age"] =age
	d["course"]=course
	student_data.append(d)
	print(student_data)


student_data = [
	{"Name": "Ram",
	"Rollno" :2,
	"Age":34,
	"course": "Python"
  },
  {"Name": "jam",
	"Rollno" :1,
	"Age":323,
	"course": "c"
  }
]


add("syam",22,18,"c++",student_data)

