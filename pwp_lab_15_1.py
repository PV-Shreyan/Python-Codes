import sqlite3
# Connect to database (or create it)
conn = sqlite3.connect ('multiple_student_subjects.db')
# Create a cursor object using the cursor() method
cursor = conn.cursor ()

# Drop old table for clean start
cursor.execute ('DROP TABLE IF EXISTS multiple_student_subjects')

# Create table with composite primary key
cursor.execute ('''
    CREATE TABLE multiple_student_subjects (
        Enrollment INTEGER,
        name TEXT NOT NULL,
        Subject TEXT NOT NULL,
        Mark INTEGER NOT NULL,
        PRIMARY KEY (Enrollment, Subject)
    )
''')
conn.commit ()

# Student records
multiple_student_subjects = [
    (92400133082, 'Palukuri Venkata Shreyan', 'PWP', 96),
    (92400133082, 'Palukuri Venkata Shreyan', 'ICE', 97),
    (92400133082, 'Palukuri Venkata Shreyan', 'DMGT', 95),
    (92400133082, 'Palukuri Venkata Shreyan', 'DSC', 89),
    (92400133082, 'Palukuri Venkata Shreyan', 'SS', 87),
    (92400133082, 'Palukuri Venkata Shreyan', 'SPDT', 88),
    (92400133082, 'Palukuri Venkata Shreyan', 'APTI', 85),
    (92400133082, 'Palukuri Venkata Shreyan', 'COA', 86)
]
cursor.executemany('''
    INSERT INTO multiple_student_subjects (Enrollment, name, Subject, Mark) 
    VALUES (?, ?, ?, ?)
''', multiple_student_subjects)
conn.commit ()

# Fetch all records
cursor.execute ('SELECT * FROM multiple_student_subjects')
rows = cursor.fetchall ()
print ("All Student Subjects Records:")
for row in rows:
    print (row)

# Subjects with Marks > 90
cursor.execute ('SELECT name, Subject, Mark FROM multiple_student_subjects WHERE Mark > 90')
high_marks = cursor.fetchall ()
print ("\nSubjects with Marks greater than 90:")
for subject in high_marks:
    print (subject)

# Update Mark for COA
cursor.execute ('''
    UPDATE multiple_student_subjects 
    SET Mark = 98 
    WHERE Enrollment = 92400133082 AND Subject = 'ICE'
''')
conn.commit ()

# Verify the update
cursor.execute ('''
    SELECT Subject, Mark FROM multiple_student_subjects 
    WHERE Enrollment = 92400133082 AND Subject = 'ICE'
''')
updated = cursor.fetchone ()
print (f"\nUpdated Mark for COA: {updated[1]}")

# Delete marks for 'SS' subject
cursor.execute ('''
    DELETE FROM multiple_student_subjects 
    WHERE Enrollment = 92400133082 AND Subject = 'DMGT'
''')
conn.commit ()

# Verify deletion
cursor.execute ('''
    SELECT * FROM multiple_student_subjects 
    WHERE Enrollment = 92400133082 AND Subject = 'DMGT'
''')
deleted = cursor.fetchone ()
if deleted is None:
    print ("\n' DMGT ' subject record has been successfully deleted")

# Calculate the average Mark
cursor.execute ('''SELECT AVG(Mark) FROM multiple_student_subjects''')
avg_mark = cursor.fetchone ()[0]

print (f"\nThe average mark of students is: {avg_mark:.2f}")

# Close the connection
conn.close ()


