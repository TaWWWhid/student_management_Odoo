# Student Management Module – Odoo 18

## 📌 Overview
This is a custom Odoo 18 module called **Student Management**.  
It manages Students, Courses, and Enrollments using a **many-to-many relation**.  

### Key Features
- Manage **Students** (Name, Email, Roll No, Department).  
- Manage **Courses** (Name, Code, Credit).  
- Enroll students in multiple courses.  
- View all students of a course and all courses of a student.  
- Smart buttons for quick navigation.  
- Menus: **Student Management → Students / Courses**.  

---

## ⚙️ Steps to Install and Build the Module

1. **Configure Odoo Service**  
   - Changed the Odoo service from *Automatic* to *Manual* in **services.msc**  
     (Press `Win + R` → type `services.msc` → Enter → find *Odoo Service* → Right-click → Properties → set **Startup type = Manual**).  
   - This gave me more control over starting and stopping the Odoo server.  

2. **Set File Permissions**  
   - Used Command Prompt to give **Full Control** permission to all Odoo directories.  
   - *(If you have permission, you can also do this via Properties → Security tab. Otherwise, use `icacls` command in CMD.)*  

3. **Python Interpreter Setup**  
   - Configured the IDE (PyCharm) to use Odoo’s local `python.exe`.  

4. **Odoo Configuration**  
   - In the `server` folder, used `odoo-bin` with `odoo.conf`.  
   - Updated `odoo.conf` with database details and addons path.  

5. **Custom Addons Directory**  
   - Created **`custom_addons`** inside the Odoo server folder.  
   - Updated `odoo.conf`:  
     ```ini
     addons_path = C:\Program Files\Odoo 18.0.20250917\server\odoo\addons,
                   C:\Program Files\Odoo 18.0.20250917\server\custom_addons
     ```  

6. **Creating the Module**  
   - Inside `custom_addons`, created `student_management` subdirectory.  
   - Added `__init__.py` and `__manifest__.py`.  
   - Restarted the server → updated Apps list → found the module.  

7. **Fixing Errors**  
   - At first, the module failed to install because of a manifest error.  
   - After correcting syntax and paths, the module installed successfully.  

8. **Building the Module**  
   - Models created: **Student** and **Course**.  
   - **Student fields:** Name, Email, Roll No, Department.  
   - **Course fields:** Name, Code, Credit.  
   - Implemented a **many-to-many relation** between students and courses.  
   - Added form views, list views, menus, and smart buttons.  

9. **Testing in Odoo**  
   - Updated Apps List → Installed module → Tested course creation, student creation, and enrollments.  

---

## 🚩 Problems I Faced and How I Solved Them

- **Permission Denied**  
  - *Problem:* Could not create/edit files in Odoo directories.  
  - *Solution:* Used `icacls` command in CMD to grant full control permissions.  

- **Manifest Error**  
  - *Problem:* Module was visible in Apps but failed to install due to manifest syntax.  
  - *Solution:* Fixed formatting in `__manifest__.py`.  

- **Invalid View Type**  
  - *Problem:* Error “Invalid view type: tree” when loading views.  
  - *Solution:* Changed `<tree>` to `<list>` (Odoo 18 standard).  

- **Context Error**  
  - *Problem:* Creating a student from the Course form caused errors.  
  - *Solution:* Used Python `default_get()` to safely set defaults instead of XML context.  

- **Smart Button Issue**  
  - *Problem:* Smart buttons did not filter records correctly.  
  - *Solution:* Wrote Python methods `action_view_students` and `action_show_enrolled_courses` with proper domains and view modes.  

---

## ▶️ Usage Example

1. Go to **Student Management → Courses**  
   - Create Course: *Algorithms* (Code: CS101, Credit: 3).  
   - Create Course: *Database Theory* (Code: CS102, Credit: 3).  

2. Go to **Student Management → Students**  
   - Create Student: *Tawhid* (with Roll No, Email, Department).  
   - In *Enrolled Courses*, select *Algorithms* and *Database Theory*.  

3. Go back to **Courses**  
   - Open *Algorithms* → Click *View Students*.  
   - The enrolled students appear here.  

4. Open a Student  
   - Click *Enrolled Courses* smart button.  
   - The linked courses appear.  

👉 This confirms that the many-to-many relation works both ways.  

---

