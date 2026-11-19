# 🎓 TUM Graduation Ceremony: A Curious Student's Event Analysis

[![Python](https://img.shields.io/badge/Python-3.10%2B-blue.svg?logo=python&logoColor=white)](#)
[![Dataset](https://img.shields.io/badge/Transcript-1%2C641_Lines-blueviolet.svg)](#)
[![Duration](https://img.shields.io/badge/Video_Length-3h_45m-orange.svg)](#)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](#)

> *"Ahead of our graduation ceremony at the Technical University of Mombasa (TUM), I wanted to understand the full flow of the event: how the day is structured, when each school and level of study is called, and the exact moment graduates flip their tassels. Instead of waiting around for the printed booklet, I decided to analyze the livestream recording as a simple data project."*

---

## 💡 The Premise

Regardless of whether you are graduating with a **Certificate, Diploma, Bachelor's, Master's, or PhD**, every student and visiting family member asks the same practical questions:
* *How long are the speeches before degree conferrals actually start?*
* *In what order do the different schools and faculties get called?*
* *When does each group stand, and when do we sit back down?*
* *When is the official moment to move the cap tassel from right to left?*

Instead of scrubbing blindly through a **3-hour-and-45-minute YouTube video** (`13,528 seconds`), this project uses simple scripting and text processing to turn the entire raw transcript into a structured, chronological guide.

---

## 🛠️ How It Works (Simple Methods & AI Tools)

I kept the approach practical and lightweight:

1. **Transcript Ingestion (with AI Assistance):**
   * Standard CLI downloaders ran into YouTube's automated `429 Too Many Requests` rate-limits.
   * I used an AI assistant running a browser session to access the video's transcript panel directly and pull the raw timestamped text (1,641 lines).
2. **Timestamp Normalization:**
   * Wrote a small Python helper to convert `[MM:SS]` and `[HH:MM:SS]` markers into raw seconds.
   * This allowed easy calculation of phase durations (e.g., speeches vs. award ceremonies).
3. **Sequential Phase Detection:**
   * A Python script (`analyze_graduation.py`) scans line-by-line for transition markers (e.g., academic procession, anthem cues, school dean introductions, conferment formulas, and dissolution).
   * By enforcing a forward-only order, the script maps the continuous stream into 18 distinct ceremonial phases.
4. **Generalization Across All Faculties:**
   * Rather than focusing on just one course, the script maps every academic division: Doctorates, Master's, Certificates, Diplomas, and all six undergraduate schools.

---

## ⏱️ Complete Ceremony Timeline & Event Order

Here is the full chronological progression extracted directly from the transcript:

| # | Time | Duration | Ceremonial Phase | Key Details & Spoken Cues |
| :-: | :---: | :---: | :--- | :--- |
| **01** | `00:01` – `04:00` | ~4m | **Academic Procession** | Marine Cadets and brass band march in, followed by faculty deans, senate, council, and VC. |
| **02** | `04:00` – `11:48` | ~8m | **Parade Review & Anthems** | Parade inspection; Kenya National Anthem, East African Community Anthem, and TUM Anthem. |
| **03** | `11:49` – `24:17` | ~12m | **Interfaith Opening Prayers** | Opening prayers: Sheikh Abdurrahman Said (Islamic prayer) and Rev. Julius Nudi (Christian prayer). |
| **04** | `24:18` – `25:37` | ~1m | **Constitution of Congregation** | VC Prof. Laila Abubakar: *"I declare this assembly as the 12th congregation of TUM. May you all be seated."* |
| **05** | `25:38` – `41:42` | ~16m | **Announcements & TUM Choir** | Registrar announcements; TUM Choir performs the classic song *Mateso* (by Rajab Mzee) and spoken word. |
| **06** | `41:43` – `01:06:48` | ~25m | **Valedictorian Speeches & Awards** | Recognition of top scholars: Terry Charity Wangui Mugo and Marera Nelson Mandela (Medical Lab Science). |
| **07** | `01:06:49` – `01:28:23` | ~21m | **Vice Chancellor's Address** | VC highlights the launch of Mombasa's first School of Medicine, BSc Nautical Science, and research milestones. |
| **08** | `01:28:24` – `01:37:25` | ~9m | **Council Chairman's Address** | Chairman of Council / Acting Chancellor remarks and charge to graduating scholars. |
| **09** | `01:37:26` – `01:46:00` | ~8m | **Chief Guest's Keynote** | Address on behalf of the Cabinet Secretary for Education (Hon. Julius Migos Ogamba). |
| **10** | `01:46:00` – `02:08:00` | ~22m | **PhD Degrees Conferment** | Deans present PhD candidates; Chancellor confers degrees; ceremonial hooding and dais photos. |
| **11** | `02:08:00` – `02:16:34` | ~8m | **Master's Degrees Conferment** | Roll call across Humanities, Computing, Business, Engineering, and Applied Sciences. |
| **12** | `02:16:35` – `02:23:02` | ~6m | **Institutional Certificates** | Presentation and award of technical/vocational certificates (e.g. ICT & Maintenance, Business). |
| **13** | `02:23:03` – `02:52:56` | ~30m | **University Diplomas Award** | Comprehensive diploma roll call across all constituent faculties. |
| **14** | `02:52:57` – `03:35:15` | ~42m | **Bachelor's Degrees Roll Call** | Deans present undergraduate cohorts in order: Computing $\to$ Applied Sciences $\to$ Business $\to$ Engineering $\to$ Humanities $\to$ Maritime. |
| **15** | `03:35:16` – `03:38:03` | ~3m | **Medical Ethics Oath** | Medical Laboratory Science graduates stand and take their professional code of ethics. |
| **16** | `03:38:04` – `03:40:59` | ~3m | **Bachelor's Degree Admission** | Chancellor confers degrees: *"I admit the persons presented to me..."* **$\rightarrow$ All Bachelor's flip tassels from Right to Left!** |
| **17** | `03:41:00` – `03:41:53` | ~1m | **Dissolution of Congregation** | Chancellor: *"I declare the 12th congregation dissolved."* |
| **18** | `03:41:54` – `03:44:13` | ~2m | **Closing Anthem & Recession** | Final Kenya National Anthem; celebration; academic procession departs. |

---

## 🎓 Degree Hierarchy & Faculty Presentation Order

Degrees follow strict academic seniority:
$$\text{PhD} \longrightarrow \text{Master's} \longrightarrow \text{Certificates} \longrightarrow \text{Diplomas} \longrightarrow \text{Bachelor's}$$

### Undergraduate Presentation Sequence (`[02:52:57]` – `[03:35:15]`):
When the undergraduate roll call begins, the Deans present their candidates in this exact sequence:
1. **Institute of Computing and Informatics (ICI):** `[02:53:42]` *(BSIT, BSc Computer Science)*
2. **School of Applied and Health Sciences (SAHS):** `[02:57:07]` *(Medical Lab Science, Food Science, Marine Resource Management)*
3. **School of Business (SOB):** `[03:02:35]` *(BCom, BBA, Human Resources, Procurement & Supply Chain)*
4. **School of Engineering and Technology (SET):** `[03:10:55]` *(Civil, Electrical, Mechanical, Building Engineering)*
5. **School of Humanities and Social Sciences (SHSS):** `[03:23:33]` *(Mass Communication, Development Studies, Counseling)*
6. **Institute of Maritime and Seafaring Studies (IMSS):** `[03:33:04]` *(BSc Nautical Science, Maritime Management)*

---

## 🎯 Universal Etiquette & Cues for Any Graduate

No matter your program, keep these universal rules in mind:

1. **Before Conferment (Tassel on the RIGHT):**
   * Wear your mortarboard (cap) flat. Your tassel stays on the **RIGHT** side of your face throughout the entire morning.
2. **When Your School/Level is Called:**
   * When your Dean or Director steps to the microphone and reads your degree classification, **stand up at your seat**.
   * Remain standing until the announcer instructs: *"Graduates, please take your seats until the conferment of the respective degrees."*
3. **The Big Conferment & Tassel Flip (`~03:38:00`):**
   * When the Master of Ceremonies invites all graduates of your level to rise, stand up together.
   * Listen for the Chancellor's formal words: *"I admit the persons presented to me to the respective degrees of Technical University of Mombasa, and by my authority and that of the Senate, give power to read and to do all that appertains to this degree..."*
   * **Flip your tassel from the RIGHT side to the LEFT side.** You are now an official graduate! 🎉
4. **Recession Protocol:**
   * Stand through the closing National Anthem and remain standing at your seat until the Chancellor, Council, and faculty procession completely departs the pavilion.

---

## 💻 Running the Script Locally

```bash
# Clone the repository
git clone https://github.com/userken-arch/tum_graduation_useless_analysis.git
cd tum_graduation_useless_analysis

# Print the full chronological event table
python analyze_graduation.py

# Or export to structured JSON
python analyze_graduation.py --json > ceremony_timeline.json
```

---

## 📝 Conclusion

Sure, waiting for the printed PDF programme would have been much easier, but turning a long livestream recording into a clean, searchable timeline using a bit of Python and AI assistance was a fun, practical way to prepare for graduation day. 

Congratulations to all 3,281 graduates of the TUM Class of 2025 across all schools and disciplines! 🎓🚀
