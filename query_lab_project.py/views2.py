

def example_solution(request):

    students = Student.objects.all()

    for student in students:
        print(
            f'First Name: {student.first_name} Last Name: {student.last_name} GPA: {student.gpa}')

    return complete(request)



def problem_one(request):
  gpa = Student.objects.all()

  gpa.filter(gpa = 3.0).order_by(gpa)
  
  print (f"Full Name: {Student.first_name, Student.last_name} GPA: {gpa}")
  return complete(request)



def problem_two(request):
 hire_date = Instructor.objects.all()
  
 hire_date.filter(hire_date_iso = 2010).order_by(hire_date)

 for hire_date in Instructor:
    print(f"Full Name: {Instructor.first_name, Instructor.last_name} Date of Hire: {hire_date} " )
 
  
 return complete(request)



def problem_three(request):
  Course.objects.get(primary_key = 2)
  for course in StudentCourse:

   print(f"Name: {Instructor.first_name, Instructor.last_name} Course {Course}")


  return complete(request)



def problem_five(request):
  Student.objects.create(first_name = "Mitch" , last_name = "Mccasland" )
  ID = 11
  year = 2022
  GPA = 3.0
  print(f"First Name {Student.first_name, Student.last_name} ID: {ID} Year: {year} GPA: {GPA}")
  return complete(request)



def problem_six(request):
  Student.objects.all()
  for student in Student:
   print(f"First Name: {Student.first_name} Last Name: {Student.last_name} ID: {student_id} GPA: {Student.gpa}")
    # Make sure to set this equal to the primary key of the row you just created!
  student_id = 11
  return complete(request)






def problem_seven(request):
  Student.objects.filter(student_id = 11).delete()
    # Make sure to set this equal to the primary key of the row you just created!
  student_id = 11

  try:
        student = Student.objects.get(pk=student_id)
  except ObjectDoesNotExist:
        print('Great! It failed and couldnt find the object because we deleted it!')

  return complete(request)



def bonus_problem(request):

    return complete(request)



def complete(req):
    context = view_information[req.path]
    return render(req, 'school/index.html', context)
