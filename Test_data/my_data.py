from faker import Faker
fake = Faker()

#registration credentials
first_name = fake.first_name()
last_name = fake.last_name()
email = fake.email()
password = fake.password(length = 8)

#course search text
existing_course_name = ["selenium", "nodejs"]
no_existing_course_name = "12345"
