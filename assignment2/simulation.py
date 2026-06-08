################################################################################
# Author 1:      Simon Ehart
# MatNr 1:       12438518
# Author 2:      Florian Koeberl
# MatNr 2:       12403729
# Author 3:      Florian Faedler
# MatNr 3:       12422306
# File:          simulation.py
# Description:   Contains the specified semester simulation.
# Comments:      nothing to add.
################################################################################

from datetime import date

from assignment2.course import Course
from assignment2.enrollment import Enrollment
from assignment2.grade import Grade
from assignment2.gradeevaluator import GradeEvaluator
from assignment2.professor import Professor
from assignment2.student import Student
from assignment2.teachingassistant import TeachingAssistant


def main() -> None:
    print("1. Setup")

    course1 = Course("706089", "Informatics 2", 4, "English")
    course2 = Course("706090", "Mathematics", 5, "English")
    course3 = Course("706091", "Physics", 4, "English")

    student1 = Student(1, "Anna Mueller", "anna@student.tugraz.at", "2001-01-01", "Graz", 12345678, "BME")
    student2 = Student(2, "Max Bauer", "max@student.tugraz.at", "2002-02-02", "Vienna", 23456789, "BME")
    student3 = Student(3, "Lisa Huber", "lisa@student.tugraz.at", "2003-03-03", "Linz", 34567890, "BME")

    professor1 = Professor(4, "Prof. Smith", "smith@tugraz.at", "1970-01-01", "Graz", "HCC", "Room 101")
    professor2 = Professor(5, "Prof. Brown", "brown@tugraz.at", "1975-01-01", "Vienna", "Math", "Room 102")

    assistant = TeachingAssistant(
        6,
        "Tom Assistant",
        "tom@student.tugraz.at",
        "2000-04-04",
        "Graz",
        45678901,
        "BME",
        "HCC",
        "Room 103",
        course1,
    )

    print(student1.info())
    print(professor1.info())
    print(assistant.info())
    print(professor2.info())

    print("\n2. Enrollment")

    enrollment1 = Enrollment(student1, course1, "SS2026")
    enrollment2 = Enrollment(student1, course2, "SS2026")
    enrollment3 = Enrollment(student2, course1, "SS2026")
    enrollment4 = Enrollment(student2, course3, "SS2026")
    enrollment5 = Enrollment(student3, course2, "SS2026")
    enrollment6 = Enrollment(student3, course3, "SS2026")

    enrollments = [enrollment1, enrollment2, enrollment3, enrollment4, enrollment5, enrollment6]

    print(Enrollment.enrollment_summary())

    print("\n3. Grading")

    for enrollment in enrollments:
        _ = enrollment << Grade("Midterm", 4.0, date(2026, 5, 20), 0)
        _ = enrollment << Grade("Final", 5.0, date(2026, 6, 10), 0)

    print(enrollment1)

    print("\n4. Querying")

    print(enrollment1(4.5))

    print("\n5. Evaluation")

    evaluator = GradeEvaluator(4.0)
    print(evaluator(enrollments))

    print("\n6. Export")

    print(course1.to_dict())
    print(enrollment1.grades[0].to_dict())

    print("\n7. Comparison")

    print(sorted([student3, student1, student2]))
    print(sorted(enrollment1.grades))


if __name__ == "__main__":
    main()
