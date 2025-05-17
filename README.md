# 🧑‍🎓 Student Attendance Monitoring System

A dynamic, real-time web application designed for efficient student attendance tracking. This system uses Firebase Realtime Database to store and retrieve student attendance records, enabling instructors and institutions to manage class presence, sessions, and verification.

Built using HTML, CSS, JavaScript, and Firebase.

---

## 🔍 Features

### ✅ 1. Attendance Form

Students can submit attendance with key fields:
- Name
- Matriculation/Registration Number
- Subject / Programme
- Semester & Graduation Year
- Date
- Session

Includes modes for:
- **Insert:** Add new attendance records  
- **Update:** Modify existing records  
- **Delete:** Remove entries  
- **Find:** Retrieve and display previous session records

**🖼️ UI Screenshot**  
![Attendance Form UI](https://i.imgur.com/QXD8sKI.png)

---

### 📑 2. Multi-Session Support

Attendance data is grouped by sessions (e.g., Session1, Session2). Each session node is dynamically created in Firebase based on user selection, allowing for:

- Multiple session tracking
- Easy organization of attendance logs

---

### 🔐 3. Verification Page

A simple verification module is used to authenticate student submissions before redirecting to the main app.

- Generates a random 6-digit alphanumeric code
- Stores it securely in Firebase
- Allows time-limited session access


---

### 🔎 4. Attendance Finder

Admins or instructors can search for attendance records by Registration Number to:
- View detailed info (name, subject, graduation year, etc.)
- Count attendance frequency
- Identify missing or duplicate entries


---

## 🔧 Technologies Used

| Tool / Tech       | Description                                |
|-------------------|--------------------------------------------|
| **HTML/CSS/JS**   | Frontend layout and interaction            |
| **Firebase DB**   | Real-time storage of records               |
| **Firebase Auth** | Secure session-based attendance verification |
| **Firebase Hosting (Optional)** | Easily deploy the app to web |

---
