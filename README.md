# 🎓 TUM Graduation Ceremony: A Curious Student's Analysis

[![Python](https://img.shields.io/badge/Python-3.10%2B-blue.svg?logo=python&logoColor=white)](#)
[![Dataset](https://img.shields.io/badge/Transcript-1%2C641_Lines-blueviolet.svg)](#)
[![Duration](https://img.shields.io/badge/Video_Length-3h_45m-orange.svg)](#)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](#)

> *"I am a graduating BSIT student at the Technical University of Mombasa (TUM). Ahead of our graduation, I wanted to know what actually happens during the 3.75-hour ceremony, when my school is called, and when we actually flip our tassels. Instead of just waiting for the printed booklet, I decided to analyze the full YouTube livestream transcript."*

---

## 💡 Why I Did This

Before graduation day, every student has the same practical questions:
* *How long are the speeches?*
* *In what order do faculties get called?*
* *When does my department (Institute of Computing and Informatics) stand up?*
* *When do we move the tassel from right to left?*

Instead of guessing or scrubbing through a **3-hour-and-45-minute YouTube video** (`13,528 seconds`), I treated it as a simple data extraction and scripting project.

---

## 🛠️ How It Works (Simple Methods That Helped)

I didn't build anything overly complex—just clean, straightforward scripting and basic problem-solving:

1. **Getting the Transcript (with AI assistance):**
   * Standard tools like `yt-dlp` kept getting hit with YouTube's `HTTP 429 Too Many Requests` error.
   * I used an AI assistant running a browser session to access the video's transcript panel directly and pull the raw timestamped text (1,641 lines).
2. **Timestamp Normalization:**
   * Wrote a simple helper in Python to convert `[MM:SS]` and `[HH:MM:SS]` into integer seconds.
   * This made it easy to calculate exact phase durations (e.g. how many minutes each speech took).
3. **Sequential Phase Detection:**
   * A simple Python script (`analyze_graduation.py`) loops through the transcript lines and detects transition phrases (e.g., *"cadets marching in"*, *"declare this assembly"*, *"Institute of Computing and Informatics"*, *"I admit the persons presented"*, *"dissolved"*).
   * By enforcing a forward-only order, the script maps the continuous stream into 18 distinct ceremonial phases.
4. **Data Verification:**
   * Cross-referenced the script's output against the video to confirm real timestamps and make sure no major event was skipped.

---

## ⏱️ What Actually Happens: Chronological Timeline

Here is the full breakdown of the ceremony extracted from the transcript:

| # | Time | Duration | What Happens | Key Details & Spoken Cues |
| :-: | :---: | :---: | :--- | :--- |
| **01** | `00:01` – `04:00` | ~4m | **Academic Procession** | Marine Cadets and university brass band march in, followed by deans, council, and VC. |
| **02** | `04:00` – `11:48` | ~8m | **Parade & Anthems** | Captain Talib leads parade; Kenya National Anthem, East African Anthem, and TUM Anthem. |
| **03** | `11:49` – `24:17` | ~12m | **Opening Prayers** | Interfaith prayers: Islamic prayer (Sheikh Abdurrahman Said) and Christian prayer (Rev. Julius Nudi). |
| **04** | `24:18` – `25:37` | ~1m | **Constitution of Assembly** | VC Prof. Laila Abubakar: *"I declare this assembly as the 12th congregation of TUM. May you all be seated."* |
| **05** | `25:38` – `41:42` | ~16m | **Announcements & TUM Choir** | Registrar announcements; TUM Choir performs the classic song *Mateso* (by Rajab Mzee). |
| **06** | `41:43` – `01:06:48` | ~25m | **Valedictorian Speeches** | Top scholars recognized: Terry Charity Wangui Mugo and Marera Nelson Mandela (Medical Lab Science). |
| **07** | `01:06:49` – `01:28:23` | ~21m | **Vice Chancellor's Address** | VC highlights launch of Mombasa's first School of Medicine, BSc Nautical Science, and research grants. |
| **08** | `01:28:24` – `01:37:25` | ~9m | **Council Chairman's Address** | Chairman of Council / Acting Chancellor remarks and advice to graduates. |
| **09** | `01:37:26` – `01:46:00` | ~8m | **Chief Guest's Keynote** | Address on behalf of the Cabinet Secretary for Education (Hon. Julius Migos Ogamba). |
| **10** | `01:46:00` – `02:08:00` | ~22m | **Doctorate (PhD) Conferment** | Deans present PhD candidates; Chancellor confers degrees; hooding and official photos. |
| **11** | `02:08:00` – `02:16:34` | ~8m | **Master's Degrees** | Roll call across Humanities, Computing, Business, Engineering, and Applied Sciences. |
| **12** | `02:16:35` – `02:23:02` | ~6m | **Institutional Certificates** | Presentation and award of technical/vocational certificates (e.g. ICT & Maintenance). |
| **13** | `02:23:03` – `02:52:56` | ~30m | **University Diplomas** | Comprehensive diploma roll call across all faculties. |
| **14** | `02:52:57` – `03:35:15` | ~42m | **Bachelor's Roll Call** | **1. Computing & Informatics (BSIT)**, 2. Applied Sciences, 3. Business, 4. Engineering, 5. Humanities, 6. Maritime. |
| **15** | `03:35:16` – `03:38:03` | ~3m | **Medical Ethics Oath** | Medical Laboratory Science graduates stand and take the professional ethics oath. |
| **16** | `03:38:04` – `03:40:59` | ~3m | **Bachelor's Degree Admission** | Chancellor confers degrees: *"I admit the persons presented to me..."* **$\rightarrow$ Flip tassel from Right to Left!** |
| **17** | `03:41:00` – `03:41:53` | ~1m | **Congregation Dissolved** | Chancellor: *"I declare the 12th congregation dissolved."* |
| **18** | `03:41:54` – `03:44:13` | ~2m | **Closing Anthem & Recession** | Final Kenya National Anthem; celebration; academic procession departs. |

---

## 🎯 Cheat-Sheet for BSIT Graduands

If you are graduating with a **Bachelor of Science in Information Technology (BSIT)**:

1. **Before the ceremony:** Your tassel starts on the **RIGHT** side of your cap.
2. **We are called first (`~02:53:00`):** When undergraduate degrees begin, the **Institute of Computing and Informatics (ICI)** is the very first school called. Stand when BSIT and your class division are announced, then sit back down when the director finishes.
3. **The Big Moment (`~03:38:00`):** All Bachelor's graduates stand together. The Chancellor says the statutory words (*"I admit the persons presented to me..."*). **Move your tassel from the RIGHT to the LEFT!** 🎉

---

## 💻 Running the Script

```bash
# Clone the repo
git clone https://github.com/userken-arch/tum_graduation_useless_analysis.git
cd tum_graduation_useless_analysis

# Run the parser to print the table
python analyze_graduation.py

# Or export to JSON
python analyze_graduation.py --format json > timeline.json
```

---

## 📝 Conclusion

Sure, finding the printed PDF programme would have been much faster, but writing a small script and using AI to turn a messy, 3.75-hour video transcript into a clean, accurate timeline was a fun, practical project to wrap up my degree. 

Congratulations to all graduates of the TUM Class of 2025! 🎓🚀
