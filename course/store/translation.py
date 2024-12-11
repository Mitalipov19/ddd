from .models import *
from modeltranslation.translator import TranslationOptions,register

@register(Course)
class CourseTranslationOptions(TranslationOptions):
    fields = ('course_name', 'description')

@register(Online_Examination_System)
class Online_Examination_SystemTranslationOptions(TranslationOptions):
    fields = ('instructions',)

@register(CourseVideo)
class CourseVideoTranslationOptions(TranslationOptions):
    fields = ('course_video', 'course_image')

@register(Lesson)
class LessonTranslationOptions(TranslationOptions):
    fields = ('lesson_name', 'content')

@register(LessonVideo)
class LessonVideoTranslationOptions(TranslationOptions):
    fields = ('lesson_video', 'lesson_image')

@register(Homework)
class HomeworkTranslationOptions(TranslationOptions):
    fields = ('topic_name', 'description')

@register(Courses)
class CoursesTranslationOptions(TranslationOptions):
    fields = ('curses_name',)

@register(Exam)
class ExamTranslationOptions(TranslationOptions):
    fields = ('exam_name',)

@register(Questions)
class QuestionsTranslationOptions(TranslationOptions):
    fields = ('topic_name', 'text', 'Option_A', 'Option_B',
              'Option_C', 'correct_answer', 'correct_option')

@register(Certificate)
class CertificateTranslationOptions(TranslationOptions):
    fields = ('certificate_url',)
