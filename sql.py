import sqlite3

# Connect to SQLite database (creates a new database if it doesn't exist)
conn = sqlite3.connect('student.db')
cursor = conn.cursor()

# Create Student table
cursor.execute('''
    CREATE TABLE IF NOT EXISTS Student (
        student_id INTEGER PRIMARY KEY,
        name TEXT NOT NULL,
        class INTEGER NOT NULL,
        stream TEXT,
        marks FLOAT
    )
''')

# Insert sample data
sample_students = [
(1, 'John Doe', 12, 'Science', 85.5),
    (2, 'Jane Smith', 11, 'Commerce', 92.0),
    (3, 'Mike Johnson', 12, 'Arts', 78.5),
    (4, 'Emily Davis', 10, 'Science', 88.0),
    (5, 'David Wilson', 11, 'Commerce', 80.5),
    (6, 'Sophia Martinez', 12, 'Arts', 75.0),
    (7, 'Daniel Brown', 10, 'Science', 90.5),
    (8, 'Olivia Taylor', 11, 'Commerce', 87.0),
    (9, 'Liam Anderson', 12, 'Arts', 82.5),
    (10, 'Emma Thomas', 10, 'Science', 94.0),
    (11, 'James White', 11, 'Commerce', 85.0),
    (12, 'Ava Harris', 12, 'Arts', 78.0),
    (13, 'Benjamin Clark', 10, 'Science', 89.5),
    (14, 'Mia Lewis', 11, 'Commerce', 91.5),
    (15, 'Ethan Walker', 12, 'Arts', 79.5),
    (16, 'Charlotte Hall', 10, 'Science', 92.5),
    (17, 'Alexander Allen', 11, 'Commerce', 86.0),
    (18, 'Amelia Young', 12, 'Arts', 81.5),
    (19, 'Henry King', 10, 'Science', 87.5),
    (20, 'Harper Scott', 11, 'Commerce', 90.0),
    (21, 'Lucas Green', 12, 'Arts', 74.0),
    (22, 'Evelyn Adams', 10, 'Science', 93.0),
    (23, 'Mason Nelson', 11, 'Commerce', 88.5),
    (24, 'Abigail Baker', 12, 'Arts', 76.5),
    (25, 'Logan Carter', 10, 'Science', 85.0),
    (26, 'Ella Gonzalez', 11, 'Commerce', 89.0),
    (27, 'Jacob Perez', 12, 'Arts', 77.0),
    (28, 'Lily Roberts', 10, 'Science', 91.0),
    (29, 'Michael Phillips', 11, 'Commerce', 83.5),
    (30, 'Zoe Campbell', 12, 'Arts', 80.0),
    (31, 'Samuel Evans', 10, 'Science', 86.5),
    (32, 'Scarlett Edwards', 11, 'Commerce', 93.5),
    (33, 'Matthew Collins', 12, 'Arts', 79.0),
    (34, 'Madison Stewart', 10, 'Science', 84.5),
    (35, 'Jack Morris', 11, 'Commerce', 88.0),
    (36, 'Luna Rogers', 12, 'Arts', 75.5),
    (37, 'Dylan Reed', 10, 'Science', 92.0),
    (38, 'Avery Cook', 11, 'Commerce', 90.5),
    (39, 'Ryan Morgan', 12, 'Arts', 78.5),
    (40, 'Hannah Bell', 10, 'Science', 95.0),
    (41, 'Nathan Murphy', 11, 'Commerce', 87.5),
    (42, 'Leah Bailey', 12, 'Arts', 80.5),
    (43, 'Isaac Cooper', 10, 'Science', 89.0),
    (44, 'Penelope Richardson', 11, 'Commerce', 91.0),
    (45, 'Sebastian Cox', 12, 'Arts', 74.5),
    (46, 'Victoria Howard', 10, 'Science', 93.5),
    (47, 'Elijah Ward', 11, 'Commerce', 84.0),
    (48, 'Grace Foster', 12, 'Arts', 77.5),
    (49, 'Carter Bailey', 10, 'Science', 90.0),
    (50, 'Chloe Bryant', 11, 'Commerce', 85.5),
    (51, 'Julian Russell', 12, 'Arts', 81.0),
    (52, 'Layla Griffin', 10, 'Science', 94.5),
    (53, 'Anthony Diaz', 11, 'Commerce', 89.5),
    (54, 'Nora Simmons', 12, 'Arts', 79.5),
    (55, 'Adam Hayes', 10, 'Science', 88.0),
    (56, 'Lillian Butler', 11, 'Commerce', 87.0),
    (57, 'Eli Hughes', 12, 'Arts', 75.0),
    (58, 'Zachary Peterson', 10, 'Science', 91.5),
    (59, 'Aurora Flores', 11, 'Commerce', 90.0),
    (60, 'Leo Fisher', 12, 'Arts', 78.0),
    (61, 'Sarah Kim', 10, 'Science', 92.0),
    (62, 'Daniel Long', 11, 'Commerce', 85.0),
    (63, 'Mila Powell', 12, 'Arts', 76.5),
    (64, 'Aaron Richardson', 10, 'Science', 89.5),
    (65, 'Hazel Perry', 11, 'Commerce', 83.5),
    (66, 'Christopher Bell', 12, 'Arts', 81.5),
    (67, 'Savannah Barnes', 10, 'Science', 95.5),
    (68, 'Andrew Coleman', 11, 'Commerce', 88.0),
    (69, 'Eleanor Watson', 12, 'Arts', 79.0),
    (70, 'Hunter Powell', 10, 'Science', 85.0),
    (71, 'Gabriella Brooks', 11, 'Commerce', 92.5),
    (72, 'Brayden Jenkins', 12, 'Arts', 74.0),
    (73, 'Addison Lopez', 10, 'Science', 93.0),
    (74, 'Joshua Sanders', 11, 'Commerce', 87.5),
    (75, 'Scarlett Price', 12, 'Arts', 80.0),
    (76, 'Isaiah Turner', 10, 'Science', 89.0),
    (77, 'Natalie Bryant', 11, 'Commerce', 90.0),
    (78, 'Caleb Ross', 12, 'Arts', 78.5),
    (79, 'Brooklyn Foster', 10, 'Science', 94.0),
    (80, 'Connor Torres', 11, 'Commerce', 85.5),
    (81, 'Skylar Morris', 12, 'Arts', 75.0),
    (82, 'Dominic Rivera', 10, 'Science', 92.0),
    (83, 'Violet Cox', 11, 'Commerce', 88.5),
    (84, 'Easton Kelly', 12, 'Arts', 79.5),
    (85, 'Aubrey Howard', 10, 'Science', 86.0),
    (86, 'Lincoln Perez', 11, 'Commerce', 84.0),
    (87, 'Madeline Adams', 12, 'Arts', 77.0),
    (88, 'Ezra Rogers', 10, 'Science', 91.5),
    (89, 'Peyton Carter', 11, 'Commerce', 90.5),
    (90, 'Eloise Cook', 12, 'Arts', 78.0),
    (91, 'Joseph Griffin', 10, 'Science', 95.0),
    (92, 'Sophie Russell', 11, 'Commerce', 87.0),
    (93, 'Jameson Butler', 12, 'Arts', 81.0),
    (94, 'Claire Stewart', 10, 'Science', 89.5),
    (95, 'Hudson Murphy', 11, 'Commerce', 86.5),
    (96, 'Serenity Ward', 12, 'Arts', 74.5),
    (97, 'Bentley Hughes', 10, 'Science', 93.0),
    (98, 'Nevaeh Bryant', 11, 'Commerce', 85.5),
    (99, 'Everly Cox', 12, 'Arts', 80.0),
    (100, 'Colton Barnes', 10, 'Science', 88.0)
]

cursor.executemany('INSERT INTO Student VALUES (?, ?, ?, ?, ?)', sample_students)

# Commit and close
conn.commit()

# Query all students
conn = sqlite3.connect('student.db')
cursor = conn.cursor()
cursor.execute('SELECT * FROM Student')
students = cursor.fetchall()
for student in students:
    print(student)
conn.close()

