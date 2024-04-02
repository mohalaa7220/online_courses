from .models import Course, Services


def courses_list(request):

    courses = Course.objects.prefetch_related('section_set__level_set').all()

    data = []
    for course in courses:
        course_data = {
            'course': course,
            'sections': []
        }

        for section in course.section_set.all():
            section_data = {
                'section': section,

            }

            course_data['sections'].append(section_data)

        data.append(course_data)
    return {
        'data': data
    }


# ============ Services =============
def services(request):
    services = Services.objects.all()
    return {'services': services}
