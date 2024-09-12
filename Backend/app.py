from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# Configuring SQLite Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///students.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Student Model
class Student(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    total_marks = db.Column(db.Integer, nullable=False)

# Create DB
with app.app_context():
    db.create_all()

# API to Load Student Details with Pagination
@app.route('/students', methods=['GET'])
def get_students():
    page = request.args.get('page', 1, type=int)
    page_size = request.args.get('page_size', 10, type=int)
    
    # Get the filter parameters (if any)
    filter_name = request.args.get('name', None)
    filter_marks = request.args.get('total_marks', None)
    
    # Build query with filters
    query = Student.query
    if filter_name:
        query = query.filter(Student.name.like(f"%{filter_name}%"))
    if filter_marks:
        query = query.filter_by(total_marks=filter_marks)

    # Paginate results
    paginated_students = query.paginate(page=page, per_page=page_size)

    # Serialize and return results
    students = [{
        'id': student.id,
        'name': student.name,
        'total_marks': student.total_marks
    } for student in paginated_students.items]

    return jsonify({
        'students': students,
        'total': paginated_students.total,
        'page': paginated_students.page,
        'pages': paginated_students.pages
    })

if __name__ == '__main__':
    app.run(debug=True)
