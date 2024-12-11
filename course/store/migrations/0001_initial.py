# Generated by Django 4.2.17 on 2024-12-10 05:22

from django.conf import settings
import django.contrib.auth.models
import django.contrib.auth.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import multiselectfield.db.fields
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course_name', models.CharField(max_length=60, unique=True)),
                ('course_name_ru', models.CharField(max_length=60, null=True, unique=True)),
                ('course_name_en', models.CharField(max_length=60, null=True, unique=True)),
                ('description', models.TextField()),
                ('description_ru', models.TextField(null=True)),
                ('description_en', models.TextField(null=True)),
                ('price', models.PositiveSmallIntegerField()),
                ('regis_date', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateField(auto_now=True)),
                ('level', models.CharField(choices=[('beginner', 'Beginner'), ('intermediate', 'Intermediate'), ('advanced', 'Advanced')], max_length=20)),
                ('status', models.CharField(choices=[('free', 'Free'), ('premium', 'Premium')], default='free', max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Courses',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('curses_name', models.CharField(max_length=255)),
                ('curses_name_ru', models.CharField(max_length=255, null=True)),
                ('curses_name_en', models.CharField(max_length=255, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Exam',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('exam_name', models.CharField(max_length=40)),
                ('exam_name_ru', models.CharField(max_length=40, null=True)),
                ('exam_name_en', models.CharField(max_length=40, null=True)),
                ('exam_date', models.DateTimeField(auto_now_add=True)),
                ('passing_score', models.PositiveSmallIntegerField(verbose_name='проходной балл')),
                ('duration', models.DurationField(verbose_name='Время на выполнение')),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='exams', to='store.courses')),
            ],
        ),
        migrations.CreateModel(
            name='Lesson',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lesson_name', models.CharField(max_length=35)),
                ('lesson_name_ru', models.CharField(max_length=35, null=True)),
                ('lesson_name_en', models.CharField(max_length=35, null=True)),
                ('content', models.TextField()),
                ('content_ru', models.TextField(null=True)),
                ('content_en', models.TextField(null=True)),
                ('lesson_date', models.DateTimeField()),
                ('course', models.ManyToManyField(related_name='lessons', to='store.courses')),
            ],
        ),
        migrations.CreateModel(
            name='Online_Examination_System',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('instructions', models.CharField(max_length=500)),
                ('instructions_ru', models.CharField(max_length=500, null=True)),
                ('instructions_en', models.CharField(max_length=500, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('userprofile_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('Address', models.CharField(max_length=100)),
                ('Phone_number', phonenumber_field.modelfields.PhoneNumberField(blank=True, max_length=128, null=True, region='KG')),
                ('Profile_picture', models.ImageField(upload_to='user_images/')),
                ('Bio', models.TextField()),
                ('Test_date', models.DateTimeField(auto_now_add=True)),
                ('Student_No', models.CharField(max_length=255, unique=True)),
                ('Gender', models.CharField(blank=True, choices=[('Male', 'Male'), ('Female', 'Female'), ('Other', 'Other')], max_length=10, null=True)),
                ('Date_of_Birth', models.DateField(blank=True, null=True)),
                ('Nationality', models.CharField(blank=True, max_length=50, null=True)),
                ('user_role', models.CharField(default='student', max_length=16)),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            bases=('store.userprofile',),
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Teachers',
            fields=[
                ('userprofile_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('Phone_number', phonenumber_field.modelfields.PhoneNumberField(blank=True, max_length=128, null=True, region='KG')),
                ('Linkedin', models.URLField()),
                ('Languages', models.CharField(max_length=255)),
                ('Hobbies', models.CharField(blank=True, max_length=255, null=True)),
                ('Profile_picture', models.ImageField(upload_to='teachers_images/')),
                ('Teacher_Profile', models.TextField()),
                ('Experience', models.CharField(max_length=255)),
                ('Education', models.CharField(max_length=255)),
                ('Skills', models.CharField(max_length=500)),
                ('user_role', models.CharField(default='teacher', max_length=16)),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            bases=('store.userprofile',),
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='LessonVideo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lesson_video', models.FileField(upload_to='lesson_video/')),
                ('lesson_video_ru', models.FileField(null=True, upload_to='lesson_video/')),
                ('lesson_video_en', models.FileField(null=True, upload_to='lesson_video/')),
                ('lesson_image', models.ImageField(upload_to='lesson_image/')),
                ('lesson_image_ru', models.ImageField(null=True, upload_to='lesson_image/')),
                ('lesson_image_en', models.ImageField(null=True, upload_to='lesson_image/')),
                ('lesson_data', models.DateTimeField(auto_now_add=True)),
                ('lesson', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='lessons', to='store.lesson')),
            ],
        ),
        migrations.CreateModel(
            name='CourseVideo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course_video', models.FileField(upload_to='course_video/')),
                ('course_video_ru', models.FileField(null=True, upload_to='course_video/')),
                ('course_video_en', models.FileField(null=True, upload_to='course_video/')),
                ('course_image', models.ImageField(upload_to='course_image/')),
                ('course_image_ru', models.ImageField(null=True, upload_to='course_image/')),
                ('course_image_en', models.ImageField(null=True, upload_to='course_image/')),
                ('course_data', models.DateTimeField(auto_now_add=True)),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='course_video', to='store.course')),
            ],
        ),
        migrations.CreateModel(
            name='CarCourse',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.PositiveSmallIntegerField(default=1)),
                ('cart', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='items', to='store.cart')),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='store.course')),
            ],
        ),
        migrations.CreateModel(
            name='Teachers_Schedule',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quality', multiselectfield.db.fields.MultiSelectField(choices=[('Monday', 'Monday'), ('Tuesday', 'Tuesday'), ('wednesday', 'wednesday'), ('Thursday', 'Thursday'), ('Friday', 'Friday'), ('Saturday', 'Saturday'), ('Sunday', 'Sunday')], max_length=56)),
                ('teacher', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='teacher_schedules', to='store.teachers')),
            ],
        ),
        migrations.CreateModel(
            name='Subscription',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_date', models.DateTimeField(auto_now_add=True)),
                ('end_date', models.DateTimeField()),
                ('active', models.BooleanField(default=True)),
                ('courses', models.ManyToManyField(to='store.course')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='store.student')),
            ],
        ),
        migrations.CreateModel(
            name='StudyGroup',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('study_at', models.DateTimeField(auto_now_add=True)),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='study_groups', to='store.course')),
                ('members', models.ManyToManyField(related_name='study_groups_enrolled', to='store.student')),
                ('teachers', models.ManyToManyField(related_name='study_groups_taught', to='store.teachers')),
            ],
        ),
        migrations.CreateModel(
            name='Questions',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('topic_name', models.CharField(max_length=100)),
                ('topic_name_ru', models.CharField(max_length=100, null=True)),
                ('topic_name_en', models.CharField(max_length=100, null=True)),
                ('text', models.TextField()),
                ('text_ru', models.TextField(null=True)),
                ('text_en', models.TextField(null=True)),
                ('Option_A', models.CharField(max_length=255)),
                ('Option_A_ru', models.CharField(max_length=255, null=True)),
                ('Option_A_en', models.CharField(max_length=255, null=True)),
                ('Option_B', models.CharField(max_length=255)),
                ('Option_B_ru', models.CharField(max_length=255, null=True)),
                ('Option_B_en', models.CharField(max_length=255, null=True)),
                ('Option_C', models.CharField(max_length=255)),
                ('Option_C_ru', models.CharField(max_length=255, null=True)),
                ('Option_C_en', models.CharField(max_length=255, null=True)),
                ('correct_answer', models.CharField(choices=[('A', 'Option A'), ('B', 'Option B'), ('C', 'Option C')], max_length=1)),
                ('correct_answer_ru', models.CharField(choices=[('A', 'Option A'), ('B', 'Option B'), ('C', 'Option C')], max_length=1, null=True)),
                ('correct_answer_en', models.CharField(choices=[('A', 'Option A'), ('B', 'Option B'), ('C', 'Option C')], max_length=1, null=True)),
                ('correct_option', models.CharField(choices=[('A', 'Option A'), ('B', 'Option B'), ('C', 'Option C')], max_length=1)),
                ('correct_option_ru', models.CharField(choices=[('A', 'Option A'), ('B', 'Option B'), ('C', 'Option C')], max_length=1, null=True)),
                ('correct_option_en', models.CharField(choices=[('A', 'Option A'), ('B', 'Option B'), ('C', 'Option C')], max_length=1, null=True)),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='questions', to='store.courses')),
                ('exam', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='questions', to='store.exam')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='questions', to='store.student')),
            ],
        ),
        migrations.CreateModel(
            name='Homework',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('topic_name', models.CharField(max_length=255)),
                ('topic_name_ru', models.CharField(max_length=255, null=True)),
                ('topic_name_en', models.CharField(max_length=255, null=True)),
                ('due_date', models.DateTimeField(auto_now_add=True)),
                ('is_completed', models.BooleanField(default=False)),
                ('description', models.TextField()),
                ('description_ru', models.TextField(null=True)),
                ('description_en', models.TextField(null=True)),
                ('teacher', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='store.teachers')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='homeworks', to='store.student')),
            ],
        ),
        migrations.CreateModel(
            name='Favorite',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('register_date', models.DateTimeField(auto_now_add=True)),
                ('favorite_course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='store.course')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='favorite_user', to='store.student')),
            ],
        ),
        migrations.CreateModel(
            name='ExamResult',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('score', models.PositiveSmallIntegerField()),
                ('passed', models.BooleanField(default=False)),
                ('graded_at', models.DateTimeField(auto_now_add=True)),
                ('exam', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='store.exam')),
                ('student', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='store.student')),
            ],
        ),
        migrations.AddField(
            model_name='exam',
            name='teacher',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='store.teachers'),
        ),
        migrations.CreateModel(
            name='CourseReview',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rating', models.IntegerField(blank=True, choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')], null=True)),
                ('comment', models.TextField(blank=True, null=True)),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='course_reviews', to='store.course')),
                ('teacher', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='course_reviews_by_user', to='store.teachers')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='course_reviews', to='store.student')),
            ],
        ),
        migrations.CreateModel(
            name='CoursePricing',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('payment_date', models.DateTimeField(auto_now_add=True)),
                ('status', models.CharField(choices=[('paid', 'Paid'), ('unpaid', 'Unpaid')], default='unpaid', max_length=10)),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='store.course')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='store.student')),
            ],
        ),
        migrations.AddField(
            model_name='course',
            name='created_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='courses_created', to='store.teachers'),
        ),
        migrations.AddField(
            model_name='course',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='enrolled_courses', to='store.student'),
        ),
        migrations.CreateModel(
            name='Certificate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('issued_at', models.DateField(auto_now_add=True)),
                ('certificate_url', models.FileField(blank=True, null=True, upload_to='', verbose_name='сертификат')),
                ('certificate_url_ru', models.FileField(blank=True, null=True, upload_to='', verbose_name='сертификат')),
                ('certificate_url_en', models.FileField(blank=True, null=True, upload_to='', verbose_name='сертификат')),
                ('expiry_date', models.DateField(blank=True, null=True)),
                ('course', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='store.course')),
                ('student', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='store.student')),
            ],
        ),
        migrations.AddField(
            model_name='cart',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='cart', to='store.student'),
        ),
        migrations.CreateModel(
            name='Attendance',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('attended_at', models.DateTimeField(auto_now_add=True)),
                ('status', models.CharField(choices=[('present', 'Present'), ('absent', 'Absent')], max_length=50)),
                ('lesson', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='attendances', to='store.lesson')),
                ('student', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='store.student')),
            ],
        ),
    ]