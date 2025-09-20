{
    "name": "Student Management",
    "version": "18.0.1.0.1",  # bump to force reload
    "summary": "Manage students, courses, and enrollments",
    "category": "Education",
    "author": "Your Name",
    "license": "LGPL-3",
    "depends": ["base"],
    "data": [
        "security/ir.model.access.csv",
        "views/student_views.xml",
        "views/course_views.xml",
        "views/menu.xml",
    ],
    "assets": {
        "web.assets_backend": [
            "student_management/static/src/css/student_mgmt.css",
        ],
    },
    "images": ["static/description/icon.png"],
    "installable": True,
    "application": True,
}
