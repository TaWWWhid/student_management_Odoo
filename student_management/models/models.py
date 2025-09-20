from odoo import api, fields, models

# -------------------------
# Student
# -------------------------
class Student(models.Model):
    _name = "sms.student"
    _description = "Student"

    name = fields.Char(required=True)
    email = fields.Char()
    roll_no = fields.Char(string="Roll No")
    department = fields.Char()

    course_ids = fields.Many2many(
        "sms.course",
        "sms_student_course_rel",
        "student_id",
        "course_id",
        string="Enrolled Courses",
    )
    course_count = fields.Integer(compute="_compute_course_count")

    @api.depends("course_ids")
    def _compute_course_count(self):
        for rec in self:
            rec.course_count = len(rec.course_ids)

    @api.model
    def default_get(self, fields_list):
        """If opened from a Course (context carries default_course_id),
        auto-add that course to the student's many2many field."""
        vals = super().default_get(fields_list)
        course_id = self.env.context.get("default_course_id")
        if course_id:
            vals["course_ids"] = [(4, course_id)]
        return vals

    def action_show_enrolled_courses(self):
        """Smart button: open all courses this student is enrolled in."""
        self.ensure_one()
        return {
            "type": "ir.actions.act_window",
            "name": "Enrolled Courses",
            "res_model": "sms.course",
            "view_mode": "list,form",
            "domain": [("id", "in", self.course_ids.ids)],
            "target": "current",
        }

    def action_quick_create_course(self):
        """Open a blank Course form in a modal and auto-link back to this student."""
        self.ensure_one()
        return {
            "type": "ir.actions.act_window",
            "name": "New Course",
            "res_model": "sms.course",
            "view_mode": "form",
            "target": "new",  # modal dialog
            # Pass current student id; Course.default_get will auto-link it
            "context": {"default_student_id": self.id},
            "views": [(False, "form")],
        }


# -------------------------
# Course
# -------------------------
class Course(models.Model):
    _name = "sms.course"
    _description = "Course"

    name = fields.Char(required=True)
    code = fields.Char()
    credit = fields.Float()

    student_ids = fields.Many2many(
        "sms.student",
        "sms_student_course_rel",
        "course_id",
        "student_id",
        string="Students",
    )
    student_count = fields.Integer(compute="_compute_student_count")

    @api.depends("student_ids")
    def _compute_student_count(self):
        for rec in self:
            rec.student_count = len(rec.student_ids)

    def action_view_students(self):
        """Smart button: open all students of this course and pass context so
        a newly created student is auto-linked to this course."""
        self.ensure_one()
        return {
            "type": "ir.actions.act_window",
            "name": "Students in Course",
            "res_model": "sms.student",
            "view_mode": "list,form",
            "domain": [("course_ids", "in", self.id)],
            "target": "current",
            "context": {"default_course_id": self.id},  # for Student.default_get
        }

    @api.model
    def default_get(self, fields_list):
        """If opened from Student quick-create (default_student_id in context),
        auto-link that student to this course."""
        vals = super().default_get(fields_list)
        student_id = self.env.context.get("default_student_id")
        if student_id:
            vals["student_ids"] = [(4, student_id)]
        return vals

    def name_get(self):
        res = []
        for rec in self:
            label = f"[{rec.code}] {rec.name}" if rec.code else rec.name
            res.append((rec.id, label))
        return res
