"""Views for the main Django application."""

# pylint: disable=no-member,invalid-name,redefined-builtin,too-many-locals,unused-variable,unused-argument

from django.shortcuts import render, redirect
from .models import AboutPage, ContactPage, Student, Notice, Teacher
from .forms import StudentLoginForm


def home(request):
    """Render home page with public notices."""
    publicNotices = Notice.objects.filter(isPublic=True)
    data = {"public_notices": publicNotices}
    return render(request, 'home.html', data)


def about(request):
    """Render about page."""
    about_text = AboutPage.objects.all()
    data = {"aboutDetails": about_text}
    return render(request, 'about.html', data)


def contact(request):
    """Render contact page."""
    contact_text = ContactPage.objects.all()
    data = {"contactDetails": contact_text}
    return render(request, 'contact.html', data)


def adminPanel(request):
    """Admin dashboard."""
    if 'admin_user' in request.session:
        all_students = Student.objects.all()
        all_teachers = Teacher.objects.all()
        data = {'students': all_students, 'teachers': all_teachers}
        return render(request, 'admin/admin_panel.html', data)
    return redirect('admin_login')


def adminLogin(request):
    """Admin login."""
    if request.method == 'POST':
        admin_email = request.POST['email']
        admin_pwd = request.POST['pwd']

        if admin_email == "admin@gmail.com" and admin_pwd == "admin@123":
            request.session['admin_user'] = admin_email
            return redirect('admin_panel')
        return redirect('admin_login')

    return render(request, 'admin/admin_login.html')


def adminLogout(request):
    """Admin logout."""
    request.session.pop('admin_user', None)
    return redirect('admin_login')


def adminAbout(request):
    """Admin about page."""
    about_details = AboutPage.objects.all()
    data = {"aboutDetails": about_details}
    return render(request, 'admin/admin_about.html', data)


def updateAbout(request, id):
    """Update about page content."""
    if request.method == 'POST':
        aboutText = request.POST['text']
        about_obj = AboutPage.objects.get(id=id)
        about_obj.about = aboutText
        about_obj.save()
    return redirect('admin_about')


def adminContact(request):
    """Admin contact page."""
    contact_details = ContactPage.objects.all()
    data = {"contactDetails": contact_details}
    return render(request, 'admin/admin_contact.html', data)


def updateContact(request, id):
    """Update contact page."""
    if request.method == 'POST':
        contactAddress = request.POST['address']
        contactEmail = request.POST['email']
        contactNumber = request.POST['contact']
        contact_obj = ContactPage.objects.get(id=id)
        contact_obj.address = contactAddress
        contact_obj.email = contactEmail
        contact_obj.contact_num = contactNumber
        contact_obj.save()
    return redirect('admin_contact')


def addStudent(request):
    """Add new student."""
    if request.method == 'POST':
        fullName = request.POST['full_name']
        fatherName = request.POST['f_name']
        motherName = request.POST['m_name']
        gender = request.POST['gender']
        address = request.POST['address']
        city = request.POST['city']
        stuEmail = request.POST['stu_email']
        contactNum = request.POST['contact_number']
        dob = request.POST['dob']
        course = request.POST['course']
        studentId = request.POST['stu_id']
        studentUserName = request.POST['stu_user_name']
        studentPassword = request.POST['stu_pwd']

        add_student = Student.objects.create(
            full_name=fullName,
            father_name=fatherName,
            mother_name=motherName,
            gender=gender,
            address=address,
            city=city,
            email=stuEmail,
            contact_num=contactNum,
            date_of_birth=dob,
            course=course,
            stu_id=studentId,
            user_name=studentUserName,
            password=studentPassword
        )

        add_student.save()
    return render(request, 'admin/new_student.html')


def manageStudent(request):
    """Manage students."""
    all_students = Student.objects.all()
    data = {"students": all_students}
    return render(request, 'admin/manage_students.html', data)


def updateStudent(request, id):
    """Update student details."""
    if request.method == 'POST':
        student_obj = Student.objects.get(id=id)

        fullName = request.POST['full_name']
        fatherName = request.POST['f_name']
        motherName = request.POST['m_name']
        gender = request.POST['gender']
        address = request.POST['address']
        city = request.POST['city']
        stuEmail = request.POST['stu_email']
        contactNum = request.POST['contact_number']
        dob = request.POST['dob'] or student_obj.date_of_birth
        course = request.POST['course'] or student_obj.course
        studentId = request.POST['stu_id']
        studentUserName = request.POST['stu_user_name']
        studentPassword = request.POST['stu_pwd']

        student_obj.full_name = fullName
        student_obj.father_name = fatherName
        student_obj.mother_name = motherName
        student_obj.gender = gender
        student_obj.address = address
        student_obj.city = city
        student_obj.email = stuEmail
        student_obj.contact_num = contactNum
        student_obj.date_of_birth = dob
        student_obj.course = course
        student_obj.stu_id = studentId
        student_obj.user_name = studentUserName
        student_obj.password = studentPassword

        student_obj.save()
    return redirect('manage_students')


def deleteStudent(request, id):
    """Delete student."""
    if 'admin_user' in request.session:
        stu_obj = Student.objects.get(id=id)
        stu_obj.delete()
    return redirect('manage_students')


def addNotice(request):
    """Add notice."""
    if request.method == 'POST':
        noticeTitle = request.POST['notice_title']
        noticeContent = request.POST['notice_content']
        isPublic = request.POST['notice_status']

        add_notice = Notice.objects.create(
            title=noticeTitle,
            content=noticeContent,
            isPublic=isPublic
        )
        add_notice.save()
    return render(request, "admin/admin_notice.html")


def manageNotices(request):
    """Manage notices."""
    all_notices = Notice.objects.all()
    data = {'notices': all_notices}
    return render(request, 'admin/manage_notices.html', data)


def deleteNotice(request, id):
    """Delete notice."""
    if 'admin_user' in request.session:
        notice_obj = Notice.objects.get(id=id)
        notice_obj.delete()
    return redirect('manage_notices')


def updateNotice(request, id):
    """Update notice."""
    if request.method == 'POST':
        title = request.POST['title']
        content = request.POST['content']
        status = request.POST['status']

        notice_obj = Notice.objects.get(id=id)
        notice_obj.title = title
        notice_obj.content = content
        notice_obj.isPublic = status

        notice_obj.save()
    return redirect('manage_notices')


def addTeacher(request):
    """Add teacher."""
    if request.method == 'POST':
        full_name = request.POST['full_name']
        gender = request.POST['gender']
        email = request.POST['email']
        contact_num = request.POST['contact_number']
        qualification = request.POST['qualification']

        add_teacher = Teacher.objects.create(
            full_name=full_name,
            gender=gender,
            email=email,
            contact_num=contact_num,
            qualification=qualification
        )
        add_teacher.save()
    return render(request, 'admin/add_teacher.html')


def manageTeachers(request):
    """Manage teachers."""
    all_teachers = Teacher.objects.all()
    data = {"teachers": all_teachers}
    return render(request, 'admin/manage_teachers.html', data)


def deleteTeacher(request, id):
    """Delete teacher."""
    teacher_obj = Teacher.objects.get(id=id)
    teacher_obj.delete()
    return redirect('manage_teachers')


def studentLogin(request):
    """Student login."""
    if 'student_user' in request.session:
        return redirect('student_dashboard')

    form = StudentLoginForm()

    if request.method == "POST":
        form = StudentLoginForm(request.POST)

        if form.is_valid():
            user_name = form.cleaned_data['userName']
            student_pwd = form.cleaned_data['stuPwd']

            stu_exists = Student.objects.filter(
                user_name=user_name,
                password=student_pwd
            ).exists()

            if stu_exists:
                request.session['student_user'] = user_name
                return redirect('student_dashboard')

            form.add_error(None, "Invalid username or password")

    return render(request, 'student/student_login.html', {'form': form})


def studentDashboard(request):
    """Student dashboard."""
    if 'student_user' in request.session:
        student_in_session = Student.objects.get(
            user_name=request.session['student_user']
        )
        data = {"student": student_in_session}
        return render(request, 'student/student_dashboard.html', data)

    return redirect('student_login')


def studentLogout(request):
    """Student logout."""
    request.session.pop('student_user', None)
    return redirect('student_login')


def updateFaculty(request, id):
    """Update faculty."""
    if request.method == 'POST':
        full_name = request.POST['full_name']
        email = request.POST['email']
        contactNumber = request.POST['contact_number']
        gender = request.POST['gender']
        qualification = request.POST['qualification']

        teacher_obj = Teacher.objects.get(id=id)
        teacher_obj.full_name = full_name
        teacher_obj.email = email
        teacher_obj.contact_num = contactNumber
        teacher_obj.gender = gender
        teacher_obj.qualification = qualification
        teacher_obj.save()
    return redirect('manage_teachers')


def viewNotices(request):
    """Student view notices."""
    if 'student_user' in request.session:
        student_notice = Notice.objects.filter(isPublic=False)
        data = {"notices": student_notice}
        return render(request, 'student/view_notices.html', data)

    return redirect('student_login')


def studentSettings(request):
    """Student settings."""
    if 'student_user' in request.session:
        student_obj = Student.objects.get(
            user_name=request.session['student_user']
        )
        data = {'student': student_obj}

        if request.method == 'POST':
            currentPwd = request.POST['current_pwd']
            new_pwd = request.POST['new_pwd']
            student_obj.password = new_pwd
            student_obj.save()
            return redirect('student_dashboard')

        return render(request, "student/student_settings.html", data)

    return redirect('student_login')
