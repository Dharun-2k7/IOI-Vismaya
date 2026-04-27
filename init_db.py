from app import create_app, db
from app.models import Problem
from datetime import datetime, timezone, timedelta

app = create_app()

with app.app_context():
    db.create_all()
    
    # Check if a problem already exists
    if not Problem.query.first():
        sample_problem = Problem(
            title="Two Sum",
            statement="""
            <p>Given an array of integers <code>nums</code> and an integer <code>target</code>, return indices of the two numbers such that they add up to <code>target</code>.</p>
            <p>You may assume that each input would have exactly one solution, and you may not use the same element twice.</p>
            <p><strong>Example:</strong></p>
            <pre>Input: nums = [2,7,11,15], target = 9<br>Output: [0,1]</pre>
            <p>For this platform submission, just output the indices separated by a comma. For example: <code>0,1</code></p>
            """,
            correct_answer="0,1",
            start_time=datetime.now(timezone.utc),
            end_time=datetime.now(timezone.utc) + timedelta(days=7),
            is_active=True
        )
        db.session.add(sample_problem)
        db.session.commit()
        print("Sample problem 'Two Sum' added successfully.")
    else:
        print("Database already initialized with problems.")
